def f(a, b):
    #a = int(input("请输入a:"))
    #b = int(input("请输入b:"))
    #a = 123456789012
    #b = 123456789012
    print("a = %d, b = %d"%(a, b))
    result = 0
    for i in range(a, b+1):
        result = result ^ i
    print(result)
f(2, 4)
f(123, 456)
f(123456789012, 123456789012)
