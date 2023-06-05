def main():
    N = int(input())
    A = []
    for i in range(2, int(N**0.5) + 1):
        x = i * i
        while x <= N:
            A.append(x)
            x *= i
    print(N - len(set(A)))
main()
