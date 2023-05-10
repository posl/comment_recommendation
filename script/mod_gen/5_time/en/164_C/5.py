def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    cnt = 0
    for i in range(N):
        if i == 0:
            cnt += 1
        else:
            if S[i] != S[i - 1]:
                cnt += 1
    print(cnt)
main()

if __name__ == '__main__':
    main()