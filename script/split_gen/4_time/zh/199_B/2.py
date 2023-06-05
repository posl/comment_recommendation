def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    min = max(a)
    max = min
    for i in range(n):
        if max < b[i]:
            max = b[i]
    print(max - min + 1)
