def main():
    n,l = map(int,input().split())
    if l > 0:
        print(sum(range(l+1,l+n)))
    elif l+n <= 0:
        print(sum(range(l+n,l)))
    else:
        print(sum(range(l,l+n)))
