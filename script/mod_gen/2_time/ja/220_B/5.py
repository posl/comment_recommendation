def main():
    K = int(input())
    A, B = map(int, input().split())
    A = int(str(A), K)
    B = int(str(B), K)
    print(A*B)

if __name__ == '__main__':
    main()