def main():
    A, B, K = map(int, input().split())
    print(sorted([i for i in range(1, min(A, B)+1) if A % i == 0 and B % i == 0], reverse=True)[K-1])
