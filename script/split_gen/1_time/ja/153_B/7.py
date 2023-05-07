def main():
    h,n,*a=map(int,open(0).read().split())
    print('Yes' if h<=sum(a) else 'No')
