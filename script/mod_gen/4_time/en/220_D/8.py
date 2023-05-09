def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = [0] * 10
    for i in range(10):
        ans[i] = a.count(i)
    for i in range(n-1):
        new_ans = [0] * 10
        for j in range(10):
            for k in range(10):
                new_ans[(j+k)%10] += ans[j] * ans[k]
                new_ans[(j*k)%10] += ans[j] * ans[k]
        ans = new_ans
    for i in range(10):
        print(ans[i] % 998244353)

if __name__ == '__main__':
    main()