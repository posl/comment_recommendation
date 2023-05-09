def main():
    n = int(input())
    a = list(map(int, input().split()))
    subordinate = [0] * n
    for i in range(n - 1):
        subordinate[a[i] - 1] += 1
    for i in subordinate:
        print(i)

if __name__ == '__main__':
    main()