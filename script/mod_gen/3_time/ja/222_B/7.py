def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    print(sum([1 for a in A if a < P]))

if __name__ == '__main__':
    main()