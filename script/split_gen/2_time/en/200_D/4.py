def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    c = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if (a[i] + a[j]) % 200 == 0:
                print("Yes")
                print(1, i + 1)
                print(1, j + 1)
                return
            b[i] += a[j]
            c[j] += a[i]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if b[i] % 200 == c[j] % 200:
                print("Yes")
                print(i + 1, end=" ")
                for k in range(n):
                    if k == j:
                        continue
                    print(k + 1, end=" ")
                print()
                print(j + 1, end=" ")
                for k in range(n):
                    if k == i:
                        continue
                    print(k + 1, end=" ")
                print()
                return
    print("No")
main()
