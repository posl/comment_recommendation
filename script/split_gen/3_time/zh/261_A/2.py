def main():
    l1,r1,l2,r2 = input().split()
    l1 = int(l1)
    r1 = int(r1)
    l2 = int(l2)
    r2 = int(r2)
    if l1<=l2 and l2<r1 and r1<=r2:
        print(r1-l2)
    elif l1<=l2 and l2<r1 and r2<r1:
        print(r2-l2)
    elif l1<=l2 and r2<=r1:
        print(r2-l2)
    elif l2<=l1 and r1<=r2:
        print(r1-l1)
    elif l2<=l1 and r1<r2:
        print(r1-l1)
    elif l2<=l1 and r2<=r1:
        print(r2-l1)
    else:
        print(0)
main()
