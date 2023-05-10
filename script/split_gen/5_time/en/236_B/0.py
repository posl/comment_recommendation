def main():
    #n = 3
    #a = [1, 3, 2, 3, 3, 2, 2, 1, 1, 1, 2]
    #n = 1
    #a = [1, 1, 1]
    #n = 4
    #a = [3, 2, 1, 1, 2, 4, 4, 4, 4, 3, 1, 3, 2, 1, 3]
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    #print(len(a))
    #print(a[n-2])
    print(a[n-1])
