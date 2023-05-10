def base_10_to_n(X, n):
    if (int(X/n)):
        return base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
K = int(input())
A, B = map(int, input().split())
A = base_10_to_n(A, 10)
B = base_10_to_n(B, 10)
A = int(A, K)
B = int(B, K)
print(A*B)

if __name__ == '__main__':
    base_10_to_n()