def main():
    N = int(input())
    v = list(map(int,input().split()))
    v.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            ans = v[i]
        else:
            ans = (ans + v[i])/2
    print(ans)

if __name__ == '__main__':
    main()