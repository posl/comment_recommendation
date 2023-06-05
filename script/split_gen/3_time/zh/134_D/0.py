def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = (i + 1) % 2
    if sum(a) == 0:
        print(0)
    else:
        print(1)
        print(b.index(1) + 1)
main()
