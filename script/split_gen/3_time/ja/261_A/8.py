def main():
    l1,r1,l2,r2 = map(int,input().split())
    if (l1 <= l2 <= r1) and (l1 <= r2 <= r1):
        print(r2-l2)
    elif (l1 <= l2 <= r1) and (r1 <= r2):
        print(r1-l2)
    elif (l1 <= l2 <= r1) and (r2 <= r1):
        print(r2-l2)
    elif (l2 <= l1 <= r2) and (l2 <= r1 <= r2):
        print(r1-l1)
    elif (l2 <= l1 <= r2) and (r2 <= r1):
        print(r2-l1)
    elif (l2 <= l1 <= r2) and (r1 <= r2):
        print(r1-l1)
    else:
        print(0)
