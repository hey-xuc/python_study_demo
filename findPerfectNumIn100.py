"""
寻找1000以内的完美数
author: 徐城
"""
l = []  # 存储完美数list
for i in range(1, 1000):
    factor = [] # 存储当前i的因子list
    for j in range(1, i): 
        if i % j == 0:
            # j 为 i 的因子 存储到factor
            factor.append(j)
    # 算出因子的和  等于i就是完美数
    total = 0
    for k in range(len(factor)):
        total += factor[k]
    if total == i:  
        l.append(i)
        
print(l)