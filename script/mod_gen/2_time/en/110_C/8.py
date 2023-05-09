def main():
    S = input()
    T = input()
    #SとTの文字列を集合にして、文字数を比較する
    if len(set(S)) != len(set(T)):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()