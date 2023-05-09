def main():
    N = int(input())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            if i != 0 and i != N-1:
                if p[i-1] != i-1 and p[i+1] != i+1:
                    p[i] = i-1
                    ans += 1
            elif i == 0:
                if p[i+1] != i+1:
                    p[i] = i+1
                    ans += 1
            elif i == N-1:
                if p[i-1] != i-1:
                    p[i] = i-1
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()