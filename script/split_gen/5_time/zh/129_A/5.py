def main():
    p,q,r = [int(x) for x in input().split()]
    print(min(p+q,q+r,r+p))
