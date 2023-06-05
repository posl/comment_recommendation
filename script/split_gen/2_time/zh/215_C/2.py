def main():
    N = int(input())
    k = 0
    while N >= 2:
        N = int(N / 2)
        k += 1
    print(k)
