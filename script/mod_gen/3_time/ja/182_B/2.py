def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 1001
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    ans_num = 0
    for i in range(2, 1001):
        num = 0
        for j in range(i, 1001, i):
            num += b[j]
        if ans < num:
            ans = num
            ans_num = i
    print(ans_num)

if __name__ == '__main__':
    main()