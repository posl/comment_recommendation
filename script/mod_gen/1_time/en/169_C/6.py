def compute():
    a,b = input().split()
    a = int(a)
    b = int(b.replace('.',''))
    print(a*b//100)
compute()
