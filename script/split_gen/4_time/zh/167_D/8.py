def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    i = 1
    for j in range(k):
        i = a[i-1]
    print(i)
