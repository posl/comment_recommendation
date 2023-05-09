def main():
    X = input()
    M = int(input())
    # X が 1 桁の場合
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    # X が 2 桁以上の場合
    # X の各桁の数字を d とすると、 d+1 以上の整数 n で X を n 進法表記の数とみなして得られる値のうち、
    # M 以下であるようなものは、 d+1 以上の整数 n のうち、
    # n = d+1 となるもののみである。
    # したがって、 X の各桁の数字の最大値を d とすれば、
    # d+1 以上の整数 n のうち、
    # n = d+1 となるもののみである。
    print(int(X, int(max(X))) - int(X) + 1)

if __name__ == '__main__':
    main()