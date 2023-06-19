def main():
    n,l = map(int,raw_input().split())
    print sum(range(l+1,l+n)) - (l+1)
