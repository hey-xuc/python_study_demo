"""
判断是否是回文数
author: 徐成
"""
def isPalinrome(num):
    """
    1.将数字反转
        a.取除以十的模
        b.循环加上取模后的模，形成倒序
    2.倒序的数字与num相等为回文数
    """
    cur = 0
    tmp = num
    while tmp > 0:
        cur = cur * 10 + tmp % 10
        tmp //= 10
    return cur == num

print(isPalinrome(345))