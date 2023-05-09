def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 200 == 0:
                b.append(i+1)
                c.append(j+1)
    if len(b) == 0:
        print("No")
    else:
        print("Yes")
        print(len(b))
        print(*b)
        print(len(c))
        print(*c)
