def main():
    n = int(input())
    a = input().split()
    sum = 0
    for i in range(n):
        sum += int(a[i])
    print(sum)
