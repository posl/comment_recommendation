def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = 0
    r = 0
    for i in range(N):
        if A[i] < 0:
            l += 1
        elif A[i] > 0:
            r += 1
    if l * r >= K:
        print(A[l] * A[-r])
        return
    else:
        K -= l * r
        if K <= ((l * (l - 1)) / 2) + ((r * (r - 1)) / 2):
            if K <= ((l * (l - 1)) / 2):
                for i in range(l - 1):
                    for j in range(i + 1, l):
                        K -= 1
                        if K == 0:
                            print(A[i] * A[j])
                            return
            else:
                for i in range(r - 1):
                    for j in range(i + 1, r):
                        K -= 1
                        if K == 0:
                            print(A[-j] * A[-i])
                            return
        else:
            K -= ((l * (l - 1)) / 2) + ((r * (r - 1)) / 2)
            for i in range(l):
                for j in range(r):
                    K -= 1
                    if K == 0:
                        print(A[-j] * A[i])
                        return
