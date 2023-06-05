def main():
    n = int(input())
    h = list(map(int, input().split()))
    # print(n, h)
    count = 0
    for i in range(n):
        flag = True
        for j in range(i):
            if h[i] < h[j]:
                flag = False
                break
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()