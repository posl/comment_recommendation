def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #出力
    print(max(min(B)-max(A)+1, 0))

if __name__ == '__main__':
    main()