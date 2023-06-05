def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] == b[i]:
            count += 1
    print(count)
    count = 0
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                count += 1
    print(count)
