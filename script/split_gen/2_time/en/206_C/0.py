def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    n = 20
    a = [7, 8, 1, 1, 4, 9, 9, 6, 8, 2, 4, 1, 1, 9, 5, 5, 5, 3, 6, 4]
    a.sort()
    count = 0
    for i in range(n):
        if i == 0:
            if a[i] != a[i+1]:
                count += 1
        elif i == n-1:
            if a[i] != a[i-1]:
                count += 1
        else:
            if a[i] != a[i+1] and a[i] != a[i-1]:
                count += 1
    print(count)
