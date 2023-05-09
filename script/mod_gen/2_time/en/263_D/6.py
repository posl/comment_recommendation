def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if L > 0:
        print(sum(A) + (N - 1) * L)
    elif R < 0:
        print(sum(A) + (N - 1) * R)
    else:
        print(sum(A[:N // 2]) + L * (N // 2) + R * (N - N // 2))

if __name__ == '__main__':
    main()