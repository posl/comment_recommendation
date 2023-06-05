def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    cnt = 0
    for i in range(n):
        for j in range(i):
            if h[i] < h[j]:
                break
        else:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()