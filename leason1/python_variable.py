# 变量，以及其类型
# 1. 变量的定义
a = 1 # 整数类型
b = 2
c = a + b
print("a:", a, "b:", b)
print("a + b = ", c)

# 2. 变量的类型
# 整数类型
a = 1
print("a:", a, "type:", type(a))
# 浮点数类型
a = 1.0 # 与好多其他编程语言不同，Python可以随意直接赋值改变变量的类型
print("a:", a, "type:", type(a))

# 字符串类型
a = "Hello, World!"
print("a:", a, "type:", type(a))

# 列表类型
a = [1, 2, 3]
print("a:", a, "type:", type(a))

# 字典类型
a = {"name": "Tom", "age": 18}
print("a:", a, "type:", type(a))

# 元组类型
a = (1, 2, 3)
print("a:", a, "type:", type(a))

# 集合类型
a = {1, 2, 3}
print("a:", a, "type:", type(a))

# 布尔类型
a = True
print("a:", a, "type:", type(a))

# 空类型
a = None
print("a:", a, "type:", type(a))

# 3. 变量的命名规则
# 变量名只能包含字母、数字和下划线
# 变量名不能以数字开头
# 变量名不能包含空格
# 变量名不能包含特殊字符，如：$、@、!、%、&等
# 变量名应该具有描述性，如：name、age、gender等
# 变量名应该尽量简短，但不要太短，如：n、a、g等