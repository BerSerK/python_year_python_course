# 加减乘除
number1 = 10
number2 = 20
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)

# 取余
number1 = 10
number2 = 3
print(number1 % number2)

# 取整
number1 = 10
number2 = 3
print(number1 // number2)

# 幂运算
number1 = 2
number2 = 3
print(number1 ** number2)

# 比较运算
number1 = 10
number2 = 20
print(number1 == number2)

number1 = 10
number2 = 20
print(number1 != number2)

number1 = 10
number2 = 20
print(number1 > number2)

# 字符串运算符
# 字符串连接
string1 = "Hello, "
string2 = "World!"
print(string1 + string2)

# 重复输出字符串
string1 = "Hello, "
print(string1 * 3)

# 判断字符串是否包含在另一个字符串中
string1 = "Hello, World!"
string2 = "Hello"
print(string2 in string1)

# 判断字符串是否不包含在另一个字符串中
string1 = "Hello, World!"
string2 = "Hello"
print(string2 not in string1)

# 字符串字串
string1 = "Hello, World!"
print(string1[0])
print(string1[1:5])

# 成员运算符
# 判断元素是否在列表中
a = [1, 2, 3]
print(1 in a)

# 判断元素是否不在列表中
a = [1, 2, 3]
print(1 not in a)

# 集合运算
# 集合的并集
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b) # 并集
print(a.union(b)) # 并集
print(b.union(a)) # 并集
print(a & b) # 交集
print(a.intersection(b)) # 交集
print(b.intersection(a)) # 交集
print(a - b) # 差集
print(a.difference(b)) # 差集
print(b.difference(a)) # 差集
print(a ^ b) # 对称差集

# 逻辑运算
# 逻辑与
a = True
b = False
print(a and b)

# 逻辑或
a = True
b = False
print(a or b)

# 逻辑非
a = True
print(not a)

# 字典操作
# 字典的创建
a = {"name": "Tom", "age": 18}
print(a)

# 字典的访问
a = {"name": "Tom", "age": 18}
print(a["name"])
print(a.get("name", "佚名")) # 如果不存在，则返回默认值
print(a.get("height", 171)) # 如果不存在，则返回默认值

# 字典的修改
a = {"name": "Tom", "age": 18}
a["name"] = "Jerry"
print(a)

# 字典的删除
a = {"name": "Tom", "age": 18}
del a["name"]

# 字典的清空
a = {"name": "Tom", "age": 18}
a.clear()

# 字典的遍历
a = {"name": "Tom", "age": 18}
for key in a:
    print(key, a[key])

# 添加字典项
a = {"name": "Tom", "age": 18}
a["height"] = 178
print(a)
