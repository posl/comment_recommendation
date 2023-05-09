def main():
    S = input()
    Q = int(input())
    t, k = [], []
    for _ in range(Q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
    # 1回目の置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    # 1回目の置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    S1 = S.replace('A', 'B').replace('C', 'A').replace('B', 'C')
    # 2回目の置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    S2 = S.replace('A', 'C').replace('B', 'A').replace('C', 'B')
    # 3回目の置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    S3 = S.replace('B', 'C').replace('A', 'B').replace('C', 'A')
    # それぞれの置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    S1 = S.replace('A', 'B').replace('C', 'A').replace('B', 'C')
    S2 = S.replace('A', 'C').replace('B', 'A').replace('C', 'B')
    S3 = S.replace('B', 'C').replace('A', 'B').replace('C', 'A')
    # 1回目の置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    S1 = S.replace('A', 'B').replace('C', 'A').replace('B', 'C')
    # 2回目の置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    S2 = S.replace('A', 'C').replace('B', 'A').
