def main():
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = [a[0]]
    for i in range(1, n):
        if a[i] == a[i - 1]:
            b.append(a[i])
        elif a[i] + a[i - 1] in b:
            return print(a[i] + a[i - 1])
    print(-1)
main()
