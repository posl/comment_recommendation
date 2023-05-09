def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    Q = [int(i) for i in input().split()]
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    def lexicographic_order(n, p):
        count = 0
        for i in range(1, n):
            count += (i * factorial(n-i))
        for i in range(n):
            for j in range(1, p[i]):
                if p[i] > j:
                    count += factorial(n-i-1)
        return count + 1
    print(abs(lexicographic_order(N, P) - lexicographic_order(N, Q)))
