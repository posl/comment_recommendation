def main():
    A, B, K = map(int, input().split())
    for i in range(K):
        if A % 2 == 1:
            A -= 1
        A //= 2
        B += A
    print(A, B)

if __name__ == '__main__':
    main()