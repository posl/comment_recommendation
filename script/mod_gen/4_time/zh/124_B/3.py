def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(1, N):
        flag = True
        for j in range(i):
            if H[i] < H[j]:
                flag = False
                break
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()