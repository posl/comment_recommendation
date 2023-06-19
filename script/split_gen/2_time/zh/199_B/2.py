def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_a = max(a)
    min_b = min(b)
    print(min_b - max_a + 1 if min_b - max_a >= 0 else 0)
main()
