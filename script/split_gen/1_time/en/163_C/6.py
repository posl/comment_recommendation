def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    count = [0] * n
    for i in range(n):
        count[a[i]-1] += 1
    for i in range(n):
        print(count[i])
