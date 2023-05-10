def main():
    N, A, B = map(int, input().split())
    S = input()
    count = 0
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            if S[i] == 'a':
                count += A
            else:
                count += B
        else:
            if S[i] != 'a':
                count += min(A, B)
    if N%2 == 1:
        if S[N//2] != 'a':
            count += min(A, B)
    print(count)

if __name__ == '__main__':
    main()