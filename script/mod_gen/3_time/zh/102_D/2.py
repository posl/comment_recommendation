def main():
    n = int(input())
    a = list(map(int, input().split()))
    # print(a)
    # print(a[0:n])
    # print(a[1:n])
    # print(a[2:n])
    # print(a[3:n])
    ans = 10**9
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    max_num = max(sum(a[0:i+1]), sum(a[i+1:j+1]), sum(a[j+1:k+1]), sum(a[k+1:l+1]))
                    min_num = min(sum(a[0:i+1]), sum(a[i+1:j+1]), sum(a[j+1:k+1]), sum(a[k+1:l+1]))
                    if ans > max_num - min_num:
                        ans = max_num - min_num
    print(ans)

if __name__ == '__main__':
    main()