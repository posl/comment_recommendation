def main():
    n,k = map(int,input().split())
    #print(n,k)
    if n%k == 0:
        print(0)
    else:
        print(1)
