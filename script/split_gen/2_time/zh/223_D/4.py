def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    # A_i在P中比B_i早出现。
    # 1. A_i, B_i都在P中
    # 2. A_i在P中，B_i不在P中
    # 3. A_i不在P中，B_i在P中
    # 4. A_i, B_i都不在P中
    # 1. A_i, B_i都在P中
    # 2. A_i在P中，B_i不在P中
    # 3. A_i不在P中，B_i在P中
    # 4. A_i, B_i都不在P中
    # 1. A_i, B_i都在P中
    # 2. A_i在P中，B_i不在P中
    # 3. A_i不在P中，B_i在P中
    # 4. A_i, B_i都不在P中
    # 1. A_i, B_i都在P中
    # 2. A_i在P中，B_i不在P中
    # 3. A_i不在P中，B_i在P中
    # 4. A_i, B_i都不在P中
    # 1. A_i, B_i都在P中
    # 2. A_i在P中，B_i不在P中
    # 3. A_i不在P中，B_i在P中
    # 4. A_i, B_i都不在P中
    # 1. A_i, B_i都在P中
    # 2. A_i在P中，B_i不在P中
    # 3. A_i不在P中，B_i在P中
    # 4. A_i, B_i都不在P中
