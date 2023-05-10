def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        p = 0
        q = 0
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                p = j
                q = n // j
                break
        print(p, q)
