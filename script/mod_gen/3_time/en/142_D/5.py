def main():
    A, B = map(int, input().split())
    print(len(set(gcd(A, B))))

if __name__ == '__main__':
    main()