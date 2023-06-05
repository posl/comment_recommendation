def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N - 1):
        count = 0
        j = i
        while True:
            if P[j] - 1 == i:
                break
            count += 1
            j = P[j] - 1
        if count > ans:
            ans = count
    print(ans + 1)

if __name__ == '__main__':
    main()