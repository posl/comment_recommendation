def main():
    #n = int(input())
    #a = [int(x) for x in input().split()]
    n = 8
    a = [27,23,76,2,3,5,62,52]
    print(min([abs(sum(a[:t]) - sum(a[t:])) for t in range(1,n)]))
