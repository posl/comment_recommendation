def main():
    N, A, B = map(int, input().split())
    S = input()
    count = 0
    for i in range(N//2):
        if S[i] != S[-i-1]:
            if S[i] == 'a' or S[-i-1] == 'a':
                count += A
            else:
                count += B
    if N % 2 == 1 and S[N//2] == 'a':
        count += A
    print(count)

if __name__ == '__main__':
    main()