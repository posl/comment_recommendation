def main():
    # A, Bの入力
    A, B = map(int, input().split())
    # A, Bの積を2で割った余りが1ならYes、そうでないならNo
    if (A * B) % 2 == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()