def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    # 人iが人jに照らされているかどうか
    is_illuminated = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            is_illuminated[i][j] = is_illuminated_by(X[i], Y[i], X[j], Y[j])
    # Aに入っている人が照らすことができる人の集合
    can_illuminated = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if is_illuminated[i][j]:
                can_illuminated[i].append(j)
    # Aに入っている人が照らすことができる人の集合の和集合
    can_illuminated_set = set()
    for i in range(K):
        can_illuminated_set = can_illuminated_set | set(can_illuminated[A[i]-1])
    # Aに入っている人が照らすことができる人の集合の和集合から、Aに入っている人を引く
    can_illuminated_set = can_illuminated_set - set(A)
    # Aに入っている人が照らすことができる人の集合の和集合から、Aに入っている人を引いた人の集合
    can_illuminated_set = list(can_illuminated_set)
    # Aに入っている人が照らすことができる人の集合の和集合から、Aに入っている人を引いた人の集合の中で、
    # Aに入っている人が照らすことができる人

if __name__ == '__main__':
    main()