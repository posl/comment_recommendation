def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 >= r2 or r1 <= l2:
        print(0)
    elif l1 < l2 and r1 <= r2:
        print(r1-l2)
    elif l1 >= l2 and r1 > r2:
        print(r2-l1)
    elif l1 < l2 and r1 > r2:
        print(r2-l2)
    else:
        print(r1-l1)
