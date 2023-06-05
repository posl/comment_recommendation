def main():
    n,d = map(int,input().split())
    print(n//(d*2+1)+1 if n%(d*2+1)!=0 else n//(d*2+1))
