def problem220_a():
    a,b,c = map(int,input().split())
    for i in range(a,b+1):
        if i % c == 0:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    problem220_a()