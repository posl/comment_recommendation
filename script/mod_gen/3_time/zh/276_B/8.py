def main():
    N, M = map(int, input().split())
    # 一个dict，key是城市编号，value是与之相连的城市编号的list
    cities = {}
    # 读取M条道路
    for i in range(M):
        A, B = map(int, input().split())
        if A not in cities:
            cities[A] = [B]
        else:
            cities[A].append(B)
        if B not in cities:
            cities[B] = [A]
        else:
            cities[B].append(A)
    # 按照题目要求，打印N行
    for i in range(1, N + 1):
        if i in cities:
            print(len(cities[i]), *sorted(cities[i]))
        else:
            print(0)

if __name__ == '__main__':
    main()