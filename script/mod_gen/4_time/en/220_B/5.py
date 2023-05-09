def main():
    K = int(input())
    A, B = map(str, input().split())
    print(int(A, K) * int(B, K))

if __name__ == '__main__':
    main()