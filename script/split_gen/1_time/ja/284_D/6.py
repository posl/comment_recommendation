def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        for p in range(2, N):
            if N % p == 0:
                q = N // p ** 2
                break
        print(p, q)
