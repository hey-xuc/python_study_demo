"""

寻找100以内的素数
author:徐城
"""
l = []  # 存储素数list
for i in range(100):
    for j in range(2, i + 1):
        n = i % j
        if n == 0:
            if j == i:
                l.append(i)
            else:
                break
        
print(l)