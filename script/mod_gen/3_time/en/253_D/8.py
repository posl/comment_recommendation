def main():
    N, A, B = map(int, input().split())
    def sum_div(n):
        return (n * (n + 1)) // 2
    def sum_div_A(n):
        return A * sum_div(n // A)
    def sum_div_B(n):
        return B * sum_div(n // B)
    def sum_div_AB(n):
        return (A * B) * sum_div(n // (A * B))
    def sum_div_not_AB(n):
        return sum_div(n) - sum_div_A(n) - sum_div_B(n) + sum_div_AB(n)
    print(sum_div_not_AB(N))

if __name__ == '__main__':
    main()