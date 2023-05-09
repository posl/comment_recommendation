def main():
    N, K, A = map(int, input().split())
    print((A+K-2)%N+1)

if __name__ == '__main__':
    main()