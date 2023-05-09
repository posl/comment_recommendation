def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(0, len(a), 2):
        if a[i] != a[i+1]:
            print(a[i])
            break
