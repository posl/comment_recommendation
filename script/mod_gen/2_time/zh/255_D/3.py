def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for _ in range(q)]
    num = [0] * n
    for i in range(1,n):
        num[i] = a[i] - a[i-1]
    ans = 0
    for i in range(1,n):
        ans += abs(num[i])
    for i in range(q):
        if x[i] == 0:
            print(ans)
        else:
            if x[i] == a[0]:
                ans += abs(num[1])
                num[1] += num[0]
                num[0] = 0
            elif x[i] == a[-1]:
                ans += abs(num[-1])
                num[-2] += num[-1]
                num[-1] = 0
            else:
                for j in range(1,n):
                    if a[j-1] < x[i] <= a[j]:
                        ans -= abs(num[j])
                        num[j] += 1
                        ans += abs(num[j])
                    elif a[j] < x[i] <= a[j+1]:
                        ans -= abs(num[j])
                        num[j] -= 1
                        ans += abs(num[j])
            a = [x[i]] * n
            print(ans)

if __name__ == '__main__':
    main()