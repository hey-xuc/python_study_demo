"""
求最大公约数与最小公倍数
author: 徐成
"""

def gcd(*args):
    '''
    最大公约数
    1.先找出最小的参数
    2.递减循环参数找出公约数既是最大公约数
    '''
    al = list(args)
    mn = min(al)
    all = len(al)
    for factor in range(mn, 0, -1):
        for i in range(all):
            if al[i] % factor != 0:
                break
            elif al[i] % factor == 0 and i == (all-1):
                return factor
    
def lcm(x, y):
    '''
    最小公倍数
    '''
    return x * y // gcd(x, y)
    
    
#print('3, 5的最小公倍数 %d' % gcd(3, 5))
print(gcd(23, 11))
print(lcm(23, 11))