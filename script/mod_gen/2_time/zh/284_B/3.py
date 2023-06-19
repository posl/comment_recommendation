def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count = 0
        for j in range(n):
            if a[j] % 2 != 0:
                count += 1
        print(count)
main()
