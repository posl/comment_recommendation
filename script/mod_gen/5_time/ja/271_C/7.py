def calc():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        if a[i+1] - a[i] == 1:
            ans += 1
            break
    print(ans)
calc()

if __name__ == '__main__':
    calc()