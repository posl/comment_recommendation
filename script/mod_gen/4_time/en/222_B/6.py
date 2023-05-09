def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    print(len([i for i in A if i < P]))

if __name__ == '__main__':
    main()