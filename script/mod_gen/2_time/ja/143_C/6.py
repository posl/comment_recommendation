def main():
    N = int(input())
    S = list(input())
    if N == 1:
        print(1)
        return
    i = 0
    while i < N-1:
        if S[i] == S[i+1]:
            S.pop(i)
            N -= 1
        else:
            i += 1
    print(N)

if __name__ == '__main__':
    main()