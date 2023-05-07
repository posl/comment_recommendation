def main():
    N = int(input())
    H = list(map(int, input().split()))
    result = 0
    for i in range(N):
        if i == 0:
            result += 1
            continue
        if H[i-1] <= H[i]:
            result += 1
    print(result)

if __name__ == '__main__':
    main()