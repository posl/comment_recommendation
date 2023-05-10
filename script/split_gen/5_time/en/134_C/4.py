def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    a_max = max(a)
    for i in range(n):
        if a[i] == a_max:
            print(sorted(a)[-2])
        else:
            print(a_max)
