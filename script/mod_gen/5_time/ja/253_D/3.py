def main():
    N, A, B = map(int, input().split())
    print(sum([x for x in range(1, N+1) if x % A != 0 and x % B != 0]))

if __name__ == '__main__':
    main()