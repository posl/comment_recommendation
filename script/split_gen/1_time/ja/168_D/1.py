def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 部屋に通路が何本あるかを数える
    count = [0] * (N + 1)
    for i in range(M):
        count[A[i]] += 1
        count[B[i]] += 1
    # 部屋に通路が何本あるかを数える
    count = [0] * (N + 1)
    for i in range(M):
        count[A[i]] += 1
        count[B[i]] += 1
    # 部屋に通路が1本しかない場合は、その部屋とその通路の組み合わせを出力する
    # 部屋に通路が2本以上ある場合は、部屋1とその通路の組み合わせを出力する
    print('Yes')
    for i in range(1, N + 1):
        if count[i] == 1:
            for j in range(M):
                if A[j] == i or B[j] == i:
                    print(j + 1)
                    break
        else:
            for j in range(M):
                if A[j] == i and B[j] == 1:
                    print(j + 1)
                    break
                if B[j] == i and A[j] == 1:
                    print(j + 1)
                    break
