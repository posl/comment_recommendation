def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    for i in range(n):
        x ^= a[i]
    print(x, end="")
    for i in range(n-1):
        x ^= a[i]
        print(" " + str(x), end="")
    print()
