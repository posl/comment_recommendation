def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    # print(N, S, T)
    # 1. 找到最小的T对应的S
    # 2. 从最小的T对应的S开始，逐个找到S对应的T
    # 3. 找到S对应的T后，从该T开始，逐个找到S对应的T
    minT = min(T)
    minT_index = T.index(minT)
    # print(minT, minT_index)
    # print(S[minT_index])
    for i in range(N):
        if i == minT_index:
            print(minT)
        else:
            print(min(minT + S[minT_index], T[i]))
