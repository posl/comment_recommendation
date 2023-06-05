def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min = a[0]
    max = b[0]
    for i in range(n):
        if min < a[i]:
            min = a[i]
        if max > b[i]:
            max = b[i]
    if min > max:
        print(0)
    else:
        print(max - min + 1)
