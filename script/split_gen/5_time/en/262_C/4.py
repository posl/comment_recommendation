def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] > i+1:
            continue
        else:
            count += 1
    print(count)
