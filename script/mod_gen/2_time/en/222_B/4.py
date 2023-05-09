def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    print(len([a for a in A if a < P]))

if __name__ == '__main__':
    main()