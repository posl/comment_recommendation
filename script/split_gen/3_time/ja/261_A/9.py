def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l2 <= r1 and r2 >= l1:
        if l1 >= l2 and r1 <= r2:
            print(r1-l1)
        elif l1 <= l2 and r1 >= r2:
            print(r2-l2)
        elif l1 >= l2 and r1 >= r2:
            print(r2-l1)
        elif l1 <= l2 and r1 <= r2:
            print(r1-l2)
    else:
        print(0)
