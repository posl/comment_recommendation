def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    # print(N)
    # print(P)
    # print(Q)
    def permutation(n):
        if n == 0:
            return [[]]
        else:
            return [[i] + p for i in range(n) for p in permutation(n - 1) if i not in p]
    p_list = permutation(N)
    # print(p_list)
    p_num = 0
    q_num = 0
    for i in range(len(p_list)):
        if p_list[i] == P:
            p_num = i + 1
        if p_list[i] == Q:
            q_num = i + 1
    # print(p_num)
    # print(q_num)
    print(abs(p_num - q_num))

if __name__ == '__main__':
    main()