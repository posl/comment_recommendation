def main():
    n,x = map(int,input().split())
    v = [0] * n
    p = [0] * n
    for i in range(n):
        v[i],p[i] = map(int,input().split())
    alc = 0
    for i in range(n):
        alc += v[i] * (p[i] / 100)
        if alc > x:
            print(i+1)
            return
    print(-1)
main()
