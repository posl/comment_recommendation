def abc():
    abc = input()
    abc = int(abc)
    a = abc//100
    b = abc%100//10
    c = abc%10
    print(a+b+c)
abc()
