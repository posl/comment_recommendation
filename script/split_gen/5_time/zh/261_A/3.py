def main():
    l1,r1,l2,r2 = map(int,input().split())
    if (l2 <= l1 and l1 <= r2) or (l2 <= r1 and l1 <= r2) or (l1 <= l2 and l2 <= r1) or (l1 <= r2 and l2 <= r1):
        print(min(r1,r2)-max(l1,l2))
    else:
        print(0)
