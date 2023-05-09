def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # print(N, W)
    # print(A)
    # A1を選ぶときの重さの和のリスト
    A1 = [0]
    for i in range(N):
        tmp = []
        for j in A1:
            if j + A[i] <= W:
                tmp.append(j + A[i])
        A1.extend(tmp)
    A1.sort()
    # print(A1)
    # A2を選ぶときの重さの和のリスト
    A2 = [0]
    for i in range(N):
        tmp = []
        for j in A2:
            if j + A[i] <= W:
                tmp.append(j + A[i])
        A2.extend(tmp)
    A2.sort()
    # print(A2)
    # A1を選ぶときの重さの和のリスト
    A3 = [0]
    for i in range(N):
        tmp = []
        for j in A3:
            if j + A[i] <= W:
                tmp.append(j + A[i])
        A3.extend(tmp)
    A3.sort()
    # print(A3)
    # A1を選ぶときの重さの和のリスト
    A4 = [0]
    for i in range(N):
        tmp = []
        for j in A4:
            if j + A[i] <= W:
                tmp.append(j + A[i])
        A4.extend(tmp)
    A4.sort()
    # print(A4)
    # A1を選ぶときの重さの和のリスト
    A5 = [0]
    for i in range(N):
        tmp = []
        for j in A5:
            if j + A[i] <= W:
                tmp.append(j + A[i])
        A5.extend(tmp)
    A5.sort()
    # print(A5)
    # A1を選ぶときの重さの和のリスト
    A6 = [0]
    for i in range(N):
        tmp = []
        for j in A6:
            if j + A[i] <= W:
                tmp.append(j
