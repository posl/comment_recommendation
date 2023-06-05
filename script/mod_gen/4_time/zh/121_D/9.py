def f(a, b):
    if a == b:
        return a
    if a == 0:
        return f(1, b)
    if a % 2 == 0:
        return f(a - 1, b) ^ a
    else:
        return (f(a - 1, b) ^ a) ^ f(0, a - 1)
a = int(input("请输入a的值:"))
b = int(input("请输入b的值:"))
print("f(", a, ",", b, ")=", f(a, b))
