def main():
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))
    print(min(sum(a),sum(a[:l])+l*min(a[l:]),sum(a[:r])+r*min(a[r:])))
