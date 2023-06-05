def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    if l == 0 and r == 0:
        print(sum(a))
        return
    elif l == 0 and r != 0:
        print(sum(a) + r*len(a))
        return
    elif l != 0 and r == 0:
        print(sum(a) + l*len(a))
        return
    else:
        sum1 = sum(a) + l*len(a)
        sum2 = sum(a) + r*len(a)
        #print(sum1, sum2)
        if sum1 < sum2:
            print(sum1)
            return
        else:
            print(sum2)
            return

if __name__ == '__main__':
    main()