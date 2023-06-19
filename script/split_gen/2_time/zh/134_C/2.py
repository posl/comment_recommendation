def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    max_b = max(a[:a.index(max_a)] + a[a.index(max_a)+1:])
    for i in range(n):
        if a[i] == max_a:
            print(max_b)
        else:
            print(max_a)
