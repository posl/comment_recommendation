def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 >= r2 or l2 >= r1:
        print(0)
    else:
        print(max(0,min(r1,r2)-max(l1,l2)))
