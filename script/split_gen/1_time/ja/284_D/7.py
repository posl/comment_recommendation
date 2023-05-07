def main():
    T = int(input())
    N = [int(input()) for _ in range(T)]
    for i in range(T):
        p = 0
        q = 0
        for j in range(2, int(N[i] ** (1/2)) + 1):
            if N[i] % j == 0:
                p = j
                q = N[i] // j
                break
        print(p, q)
