'''
    寻找100 以内的斐波那契数
    author 徐城
'''

current = 1     # 当前的数
previons = 0    # 上一个数
l = []  # 初始化存储list 
while current < 100:
    res = current + previons
    l.append(res)
    previons = current
    current = res
    
print(l)