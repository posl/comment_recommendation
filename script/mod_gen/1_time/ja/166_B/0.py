def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [0] * k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        flag = 0
        for j in range(k):
            if i+1 in a[j]:
                flag = 1
        if flag == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()