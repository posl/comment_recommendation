def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A_prime = [a for a in A if a != X]
    print(*A_prime)

if __name__ == '__main__':
    main()