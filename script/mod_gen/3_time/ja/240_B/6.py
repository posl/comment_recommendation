def main():
    N = int(input())
    a = list(map(int, input().split()))
    # setを使って重複を削除
    print(len(set(a)))

if __name__ == '__main__':
    main()