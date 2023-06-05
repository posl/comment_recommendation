def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += b[a[i]-1]
        if i < n-1 and a[i] == a[i+1]-1:
            sum += c[a[i]-1]
    print(sum)
