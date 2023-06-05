def main():
    N, M = map(int, input().split())
    x = [0] * N
    y = [0] * N
    z = [0] * N
    for i in range(N):
        x[i], y[i], z[i] = map(int, input().split())
    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                sign = [1, 1, 1]
                if i == 1:
                    sign[0] = -1
                if j == 1:
                    sign[1] = -1
                if k == 1:
                    sign[2] = -1
                A = []
                for l in range(N):
                    A.append(sign[0] * x[l] + sign[1] * y[l] + sign[2] * z[l])
                A.sort(reverse=True)
                ans = max(ans, sum(A[:M]))
    print(ans)
