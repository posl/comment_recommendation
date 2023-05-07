def main():
    #入力
    N, A, B = map(int, input().split())
    #出力
    print(min(A * N, B))

if __name__ == '__main__':
    main()