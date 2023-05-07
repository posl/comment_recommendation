def main():
    n = int(input())
    a = list(map(int, input().split()))
    #a = [1, 4, 2, 5]
    #a = [3, 1, 5, 4]
    #a = [6, 13, 12, 5, 3, 7, 10, 11, 16, 9, 8, 15, 2, 1, 14, 4]
    #a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    a = list(enumerate(a))
    for i in range(n):
        for j in range(2**(n-i-1)):
            if a[2*j][1] > a[2*j+1][1]:
                a[2*j] = (-1, -1)
            else:
                a[2*j+1] = (-1, -1)
        a = [x for x in a if x != (-1, -1)]
    print(a[0][0]+1)
