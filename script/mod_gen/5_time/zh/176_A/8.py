def calc_time():
    n,x,t = input("请输入N,X,T\n").split(" ")
    n = int(n)
    x = int(x)
    t = int(t)
    if n%x == 0:
        return (n//x)*t
    else:
        return (n//x)*t+t

if __name__ == '__main__':
    calc_time()