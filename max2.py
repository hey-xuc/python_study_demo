def max2(x):
    """
    寻找list中最大的两个数
    """
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2
    
    
l = [1,23,45,234,5,6]
print(max2(l))