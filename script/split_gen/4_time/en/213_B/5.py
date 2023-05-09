def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_sorted = sorted(a, reverse=True)
    print(a.index(a_sorted[1]) + 1)
