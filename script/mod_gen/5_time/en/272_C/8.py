def solution():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    max = -1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0 and a[i] + a[j] > max:
                max = a[i] + a[j]
    print(max)
solution()

if __name__ == '__main__':
    solution()