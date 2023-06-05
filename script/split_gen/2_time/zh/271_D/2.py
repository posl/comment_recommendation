def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    #print(a)
    res = 0
    for i in range(n-1):
        if a[i] < a[i+1]:
            res += 1
    print(res+1)
