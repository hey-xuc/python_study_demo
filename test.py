scores = {'luotin': 95, 'yuanfang': 78, 'direnjie': 82} #
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 100)}
print(items1, items2, items3)
# 通过键获取字典中对应的值
print(scores['luotin'])
print(scores['direnjie'])
# 对字典中的所有键值遍历
for key in scores:
    print(f'{key}: {scores[key]}')
# 更新字典中的元素
scores['yuanfang'] = 65
scores['zhuge'] = 71
scores.update(lengmian=67, qihe=85)
print(scores)
if 'wuzetian' in scores:
    print(scores['wuzetian'])
print(scores.get('wuzetian'))
# get方法也是通过键获取对于的值但是可以设置默认值
print(scores.get('wuzetian', 60))
# 删除
print(scores.popitem())
print(scores.popitem())
print(scores.pop('luotin', 100))
print(scores)
scores.clear()
