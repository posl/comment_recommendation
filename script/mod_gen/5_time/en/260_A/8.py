def main():
    S = input()
    cnt = 0
    for i in range(3):
        if S.count(S[i]) == 1:
            print(S[i])
            cnt += 1
            break
    if cnt == 0:
        print(-1)

if __name__ == '__main__':
    main()