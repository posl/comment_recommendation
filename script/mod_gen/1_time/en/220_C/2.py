def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 10**5
    ans = 0
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        ans += 1
        if sum > X:
            break
    print(ans)

if __name__ == '__main__':
    main()