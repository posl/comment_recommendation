def main():
    N = int(input())
    S = input()
    cnt = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()