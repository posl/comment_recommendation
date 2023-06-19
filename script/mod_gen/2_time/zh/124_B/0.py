def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 1
    for i in range(1, n):
        flag = True
        for j in range(i):
            if h[j] >= h[i]:
                flag = False
        if flag:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()