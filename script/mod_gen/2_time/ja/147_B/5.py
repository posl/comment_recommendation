def main():
    S = input()
    n = len(S)
    h = n // 2
    cnt = 0
    for i in range(h):
        if S[i] != S[n - i - 1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()