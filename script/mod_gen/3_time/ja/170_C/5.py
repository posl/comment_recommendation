def main():
    X, N = map(int, input().split())
    p_list = list(map(int, input().split()))
    if N == 0:
        print(X)
        return
    for i in range(100):
        if (X - i) not in p_list:
            print(X - i)
            return
        if (X + i) not in p_list:
            print(X + i)
            return

if __name__ == '__main__':
    main()