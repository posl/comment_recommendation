def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # 1-indexed
    P = [0] + P
    # 1-indexed
    eaten = [-1] * (N + 1)
    # 1-indexed
    stack = [0] * (N + 1)
    # 1-indexed
    stack_index = [0] * (N + 1)
    for i in range(1, N + 1):
        # stack に stack_index が K 以上のカードがない場合、
        # P[i] を stack に積む
        if stack_index[K] == 0:
            stack_index[P[i]] += 1
            stack[stack_index[P[i]]] = P[i]
        else:
            # stack に stack_index が K 以上のカードがある場合、
            # P[i] が stack_index 以上のカードのうち、最小のカードの上に積む
            # その後、stack_index 以上のカードを食べる
            # これにより、stack_index が K になる
            stack_index[P[i]] = stack_index[K] + 1
            stack[stack_index[P[i]]] = P[i]
            # stack_index 以上のカードを食べる
            for j in range(stack_index[K], 0, -1):
                eaten[stack[j]] = i
                stack_index[stack[j]] = 0
            # stack_index が K になる
            stack_index[K] = K
    for i in range(1, N + 1):
        print(eaten[i])

if __name__ == '__main__':
    main()