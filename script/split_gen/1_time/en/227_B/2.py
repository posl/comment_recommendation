def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    if a[0] + a[1] == a[2]:
        print("Yes")
    else:
        print("No")
