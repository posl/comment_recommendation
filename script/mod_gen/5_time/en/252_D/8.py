def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(len(set(A)) - (1 if len(set(A)) % 2 == 0 else 0))

if __name__ == '__main__':
    main()