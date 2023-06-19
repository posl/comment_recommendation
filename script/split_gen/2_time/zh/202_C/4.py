def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    count = 0
    for i in range(n):
        count += b[c[a[i] - 1]]
    print(count)
