def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b_c = [0] * n
    for i in range(n):
        b_c[c[i]-1] += 1
    sum = 0
    for i in range(n):
        sum += b_c[b[a[i]-1]-1]
    print(sum)
