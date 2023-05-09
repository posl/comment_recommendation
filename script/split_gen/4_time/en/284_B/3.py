def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    count = 0
    for i in range(n):
        if a[i]%2 != 0:
            count += 1
    print(count)
