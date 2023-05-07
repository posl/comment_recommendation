def main():
    N = int(input())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, A, B)
    #Aokiの得票数が多い順にソート
    C = sorted([(A[i] + B[i], A[i], B[i]) for i in range(N)], reverse=True)
    #print(C)
    #TakahashiはAokiの得票数が多い順にスピーチを行う
    #Aokiの得票数が多い順にスピーチを行うと、
    #Aokiの得票数が多い順にスピーチを行った時の、
    #Takahashiの得票数が最大になる
    takahashi = 0
    aoki = 0
    for i in range(N):
        takahashi += C[i][1]
        aoki += C[i][2]
        if takahashi > aoki:
            print(i + 1)
            break
