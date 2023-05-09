def main():
    K = int(input())
    A, B = map(str, input().split())
    print(int(A, K) * int(B, K))
