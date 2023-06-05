def main():
    S = input()
    Q = int(input())
    t_k_list = [None] * Q
    for i in range(Q):
        t_k_list[i] = [int(x) for x in input().split()]
    # print(S)
    # print(Q)
    # print(t_k_list)
    for i in range(Q):
        t = t_k_list[i][0]
        k = t_k_list[i][1]
        for j in range(t):
            S = S.replace('a', 'bc')
            S = S.replace('b', 'ca')
            S = S.replace('c', 'ab')
        print(S[k - 1])

if __name__ == '__main__':
    main()