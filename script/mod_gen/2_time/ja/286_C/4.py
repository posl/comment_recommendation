def main():
    N, A, B = map(int, input().split())
    S = input()
    if A > B:
        print(0)
        return
    if N % 2 == 0:
        if S[:N//2] == S[N//2:]:
            print(0)
            return
        print(A)
        return
    if S[:N//2] == S[N//2+1:]:
        print(0)
        return
    if S[:N//2] == S[N//2:]:
        print(B)
        return
    print(A)

if __name__ == '__main__':
    main()