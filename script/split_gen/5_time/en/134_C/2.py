def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_max_index = a.index(a_max)
    for i in range(n):
        if i == a_max_index:
            print(max(a[:i] + a[i+1:]))
        else:
            print(a_max)
