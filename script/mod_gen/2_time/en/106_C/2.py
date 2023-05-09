def main():
    S = input()
    K = int(input())
    N = len(S)
    cnt = 0
    for i in range(N):
        if S[i] == '1':
            cnt += 1
            if cnt == K:
                print(1)
                return
        else:
            print(S[i])
            return

if __name__ == '__main__':
    main()