def main():
    #入力
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #最大100枚なので、1~100枚までの全探索
    for i in range(101):
        for j in range(101):
            for k in range(101):
                if i*A[0] + j*A[1] + k*A[2] == X:
                    print("Yes")
                    return
    print("No")
