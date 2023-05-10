def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    max_a = max(a)
    for i in range(n):
        if a[i] == max_a:
            print(max(a[:i] + a[i+1:]))
        else:
            print(max_a)
