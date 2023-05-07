def main():
    X = input()
    M = int(input())
    d = int(max(X))
    # d+1以上の整数nを選んでXをn進法表記の数とみなして得られる値のうち、M以下であるようなものは何種類あるか
    # 1 ≦ M ≦ 10^{18}
    # Xの最大値は9なので、nは9以下
    # 1 ≦ n ≦ 9
    # 1 ≦ n ≦ d+1
    # 1 ≦ n ≦ max(X)+1
    # nは整数である必要があるので、nはmax(X)+1以下の整数
    # 1 ≦ n ≦ max(X)+1
    # nは整数である必要があるので、nはfloor(max(X)+1)以下の整数
    # 1 ≦ n ≦ floor(max(X)+1)
    # nは整数である必要があるので、nはfloor(max(X))+1以下の整数
    # 1 ≦ n ≦ floor(max(X))
    # nは整数である必要があるので、nはfloor(max(X))以下の整数
    # 1 ≦ n ≦ floor(max(X))
    # nは整数である必要があるので、nはfloor(max(X))-1以下の整数
    # 1 ≦ n ≦ floor(max(X))-1
    # nは整数である必要があるので、nはfloor(max(X))-1以下の整数
    # 1 ≦ n ≦ floor(max(X))-1
    # nは整数である必要があるので、nはfloor(max(X))-1以下の整数
    # 1 ≦ n ≦ floor(max(X))-1
    # nは整数である必要があるので、nはfloor(max(X))-1以下の整数
    # 1 ≦ n ≦ floor(max(X))-1
    # n

if __name__ == '__main__':
    main()