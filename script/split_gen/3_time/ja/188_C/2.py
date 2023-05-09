def main():
    n = int(input())
    a = list(map(int, input().split()))
    #a = [1, 4, 2, 5]
    #n = 2
    #a = [3, 1, 5, 4]
    #n = 2
    #a = [6, 13, 12, 5, 3, 7, 10, 11, 16, 9, 8, 15, 2, 1, 14, 4]
    #n = 4
    b = [0] * (2 ** n)
    for i in range(2 ** n):
        b[i] = a[i]
    for i in range(n):
        for j in range(0, 2 ** (n - i - 1), 2):
            if b[j] > b[j + 1]:
                b[j // 2] = b[j]
            else:
                b[j // 2] = b[j + 1]
    print(b.index(min(b)) + 1)
