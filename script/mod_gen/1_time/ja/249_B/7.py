def main():
    S = input()
    if len(S) < 2 or len(S) > 100:
        print("入力エラー")
        return
    if S.islower() or S.isupper():
        print("No")
        return
    if S.isalpha() == False:
        print("入力エラー")
        return
    if len(set(S)) != len(S):
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()