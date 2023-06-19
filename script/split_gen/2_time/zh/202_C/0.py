def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    count = 0
    for i in range(1, n+1):
        count += b[c[i-1]-1] == a[i-1]
    print(count)
