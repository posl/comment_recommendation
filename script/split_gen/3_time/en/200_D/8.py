def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A[i] % 200 に対応する i を格納する配列
    modA = [[] for _ in range(200)]
    for i in range(N):
        modA[A[i] % 200].append(i + 1)
    for i in range(200):
        if len(modA[i]) >= 2:
            print("Yes")
            print(1, modA[i][0])
            print(1, modA[i][1])
            return
    print("No")
