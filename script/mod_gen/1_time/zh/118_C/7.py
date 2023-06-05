def main():
    N = int(input())
    A = list(map(int, input().split()))
    import fractions
    def gcd_list(numbers):
        return functools.reduce(fractions.gcd, numbers)
    print(gcd_list(A))

if __name__ == '__main__':
    main()