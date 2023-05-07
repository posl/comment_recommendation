def main():
    N = int(input())
    count = 0
    for p in range(2, int(N ** 0.5) + 1):
        if N < p ** 3:
            break
        if N % p == 0:
            q = N // p
            if q % p == 0:
                count += 1
    print(count)
