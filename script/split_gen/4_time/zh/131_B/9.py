def main():
    n,l = map(int,input().split())
    min_value = 1000
    for i in range(n):
        if min_value > abs(l+i):
            min_value = abs(l+i)
            index = i
    if l > 0:
        print(sum(range(l+1,l+n)))
    elif l+n-1 < 0:
        print(sum(range(l,l+n-1,-1)))
    else:
        print(sum(range(l,l+n))-index)
main()
