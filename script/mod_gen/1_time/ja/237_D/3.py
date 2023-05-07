def main():
    N = int(input())
    S = input()
    L = 0
    R = 0
    for i in range(N):
        if S[i] == 'L':
            L += 1
        else:
            R += 1
    A = [0] * (N + 1)
    if L == 0:
        for i in range(N):
            A[i + 1] = i + 1
    elif R == 0:
        for i in range(N):
            A[i] = N - i
    else:
        for i in range(N):
            if S[i] == 'L':
                A[i + 1 - L] = i + 1
            else:
                A[i + R + 1] = i + 1
    print(*A[1:])

if __name__ == '__main__':
    main()