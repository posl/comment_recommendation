def main():
    K = int(input())
    A, B = map(str, input().split())
    A = int(A, K)
    B = int(B, K)
    print(A * B)
