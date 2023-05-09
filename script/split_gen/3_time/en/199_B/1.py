def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(min(B) - max(A) + 1 if min(B) - max(A) + 1 > 0 else 0)
