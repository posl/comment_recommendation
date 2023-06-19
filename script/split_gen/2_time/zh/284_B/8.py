def main():
    n = int(input())
    for i in range(n):
        a = int(input())
        b = list(map(int, input().split()))
        count = 0
        for j in b:
            if j % 2 == 1:
                count += 1
        print(count)
main()
