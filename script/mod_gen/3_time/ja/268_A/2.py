def main():
    #入力
    A, B, C, D, E = map(int, input().split())
    #出力
    print(len(set([A, B, C, D, E])))

if __name__ == '__main__':
    main()