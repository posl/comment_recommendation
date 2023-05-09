def main():
    N = int(input())
    S = input()
    cnt = 1
    for i in range(1, N):
        if S[i-1] != S[i]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()