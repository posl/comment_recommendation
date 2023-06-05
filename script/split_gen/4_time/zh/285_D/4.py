def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        s, t = input().split()
        a.append(s)
        b.append(t)
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == b[j] and a[j] == b[i]:
                print("Yes")
                return
    print("No")
