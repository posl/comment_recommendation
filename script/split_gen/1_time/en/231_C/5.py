def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for _ in range(q):
        x = int(input())
        index = binary_search(a, x)
        print(n - index)
