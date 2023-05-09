def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    cnt = 0
    prev = 0
    prev_cnt = 0
    for i in range(n):
        if prev != a[i]:
            cnt += prev_cnt * (prev_cnt - 1) // 2
            prev = a[i]
            prev_cnt = 1
        else:
            prev_cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()