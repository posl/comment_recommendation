def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    A_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        A_sum[i] = A_sum[i - 1] + A[i]
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if x == y:
                continue
            B = [0] * (x + 1)
            C = [0] * (y + 1)
            for i in range(1, x + 1):
                B[i] = i
            for i in range(1, y + 1):
                C[i] = i
            flag = False
            for i in range(1, x + 1):
                for j in range(1, y + 1):
                    if B[i] == C[j]:
                        flag = True
                        break
                if flag:
                    break
            if flag:
                continue
            if (A_sum[B[x]] - A_sum[B[0]]) % 200 == (A_sum[C[y]] - A_sum[C[0]]) % 200:
                print("Yes")
                print(x, end=" ")
                for i in range(1, x + 1):
                    print(B[i], end=" ")
                print()
                print(y, end=" ")
                for i in range(1, y + 1):
                    print(C[i], end=" ")
                print()
                return
    print("No")
    return
