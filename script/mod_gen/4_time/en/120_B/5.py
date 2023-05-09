def main():
    A, B, K = map(int, input().split())
    divisors = [i for i in range(1, min(A, B) + 1) if A % i == B % i == 0]
    print(divisors[-K])

if __name__ == '__main__':
    main()