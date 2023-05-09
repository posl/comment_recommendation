def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    for i in range(n):
        if a[i] != a[i+1]:
            print(a[i]+1)
            break
