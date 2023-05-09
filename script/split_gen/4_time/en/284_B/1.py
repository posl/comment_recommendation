def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        count = 0
        for j in range(n):
            if a[j] % 2 == 1:
                count += 1
        print(count)
