def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    for i in range(n):
        print(max(a[:i] + a[i+1:]))
