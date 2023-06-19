def problem149_b():
    a,b,k = map(int,input().split())
    if k <= a:
        print(a-k,b)
    elif k > a and k <= a+b:
        print(0,b-(k-a))
    elif k > a+b:
        print(0,0)

if __name__ == '__main__':
    problem149_b()