def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    cnt = 1
    for i in range(1, n):
        flag = True
        for j in range(0, i):
            if h[i] < h[j]:
                flag = False
                break
        if flag:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()