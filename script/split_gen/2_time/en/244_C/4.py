def main():
    n = int(input())
    a = [i for i in range(1, 2 * n + 2)]
    for i in range(n):
        print(a[i])
        input()
        print(a[-i - 1])
        input()
    print(a[n])
