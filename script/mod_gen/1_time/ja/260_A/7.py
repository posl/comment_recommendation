def main():
    S = input()
    if len(S) != 3:
        print('入力文字列が3文字ではありません。')
        return
    for i in range(3):
        if S.count(S[i]) == 1:
            print(S[i])
            return
    print(-1)

if __name__ == '__main__':
    main()