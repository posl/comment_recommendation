def main():
    #入力
    A, B = map(int, input().split())
    #出力
    print(max(sum(map(int, str(A))), sum(map(int, str(B)))))

if __name__ == '__main__':
    main()