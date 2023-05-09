def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        for p in range(2, int(N**0.5)+1):
            if N%p == 0:
                q = N//p
                break
        print(p, q)
