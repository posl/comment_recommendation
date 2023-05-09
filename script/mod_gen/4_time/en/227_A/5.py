def main():
    N, K, A = map(int, input().split())
    print((K // N + (K % N >= A)) % N or N)

if __name__ == '__main__':
    main()