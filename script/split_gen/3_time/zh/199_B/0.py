def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    min_b = min(B)
    max_a = max(A)
    print(max(0, min_b - max_a + 1))
