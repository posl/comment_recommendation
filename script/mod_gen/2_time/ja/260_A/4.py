def main():
    S = input()
    for i in range(len(S)):
        if S.count(S[i]) == 1:
            print(S[i])
            return
    print(-1)

if __name__ == '__main__':
    main()