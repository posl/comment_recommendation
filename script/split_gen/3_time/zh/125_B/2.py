def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if v[i] - c[i] > 0:
            sum += v[i] - c[i]
    print(sum)
