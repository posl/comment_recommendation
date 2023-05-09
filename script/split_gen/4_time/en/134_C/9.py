def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    max_a = max(a)
    max_index = a.index(max_a)
    for i in range(n):
        if i == max_index:
            print(max(a[:i] + a[i + 1:]))
        else:
            print(max_a)
