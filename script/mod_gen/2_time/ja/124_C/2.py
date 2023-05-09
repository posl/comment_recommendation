def main():
    S = input()
    N = len(S)
    if N == 1:
        print(0)
        return
    cnt = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt += 1
    print((cnt+1) // 2)
    return

if __name__ == '__main__':
    main()