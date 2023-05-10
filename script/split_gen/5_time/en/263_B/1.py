def main():
    n = int(input())
    p = list(map(int, input().split()))
    max = 0
    for i in range(n):
        count = 0
        j = i
        while j != -1:
            j = p[j] - 1
            count += 1
        if max < count:
            max = count
    print(max)
