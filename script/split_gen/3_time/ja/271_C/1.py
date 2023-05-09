def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    n = 6
    a = [1, 2, 4, 6, 7, 271]
    #n = 10
    #a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    #n = 1
    #a = [5]
    a.sort()
    print(a)
    #a = [1, 2, 4, 6, 7, 271]
    #a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    #a = [5]
    count = 0
    for i in range(n):
        if a[i] > i + 1:
            count = i
            break
        if i == n - 1:
            count = n
    print(count)
