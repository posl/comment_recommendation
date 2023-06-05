def cal(n):
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    return a*100+b*10+c+a*10+b+c+a+b*100+c*10+b
