def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    for i in range(n):
        if a[i] == a_max:
            print(max(a[:i] + a[i+1:]))
        else:
            print(a_max)
