def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        for j in range(2, int(N**0.5)+1):
            if N % j == 0:
                p = j
                q = N // p // p
                print(p, q)
                break
