# 1. if 逻辑
a = 1
if a == 1:
    print("a == 1")
elif a == 2:
    print("a == 2")
else:
    print("a != 1")

# 2. for 逻辑
a = [1, 2, 3]
for i in a:
    print(i)

# 3. while 逻辑
a = 1
while a < 10:
    print(a)
    a += 1

# 4. break 逻辑
a = 1
while a < 10:
    print(a)
    if a == 5:
        break
    a += 1

# 5. continue 逻辑
a = 1
while a < 10:
    a += 1
    if a == 5:
        continue
    print(a)

# 6. pass 逻辑
a = 1
if a == 1:
    pass
else:
    print("a != 1")

# 7. match 逻辑, 和C++里面的switch case类似
a = 1
match a:
    case 1:
        print("a == 1")
    case 2:
        print("a == 2")
    case _:
        print("a != 1 and a != 2")
        