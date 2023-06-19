def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for x in range(1, 1001):
        if all(a[i] <= x <= b[i] for i in range(n)):
            count += 1
    print(count)
