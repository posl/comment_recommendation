def main():
    N = int(input())
    x = [0]*N
    y = [0]*N
    p = [0]*N
    for i in range(N):
        x[i], y[i], p[i] = map(int, input().split())
    S = 0
    while True:
        flag = True
        for i in range(N):
            for j in range(N):
                if p[i]*S >= abs(x[i]-x[j])+abs(y[i]-y[j]):
                    flag = False
        if flag:
            break
        else:
            S += 1
    print(S)

if __name__ == '__main__':
    main()