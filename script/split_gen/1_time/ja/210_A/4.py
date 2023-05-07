def main():
    n, a, x, y = map(int, input().split())
    sum = 0
    for i in range(1,n+1):
        if i <= a:
            sum += x
        else:
            sum += y
    print(sum)
