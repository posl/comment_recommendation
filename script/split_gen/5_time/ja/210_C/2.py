def main():
    n,k = map(int, input().split())
    c = list(map(int, input().split()))
    #print(n,k,c)
    #print(len(c))
    #print(len(set(c)))
    #print(len(c)-len(set(c)))
    #print(n-k)
    #print(len(c)-len(set(c)) - (n-k))
    if k == 1:
        print(1)
        exit()
    if len(c)-len(set(c)) - (n-k) < 0:
        print(len(set(c)))
        exit()
    print(len(set(c)) - (len(c)-len(set(c)) - (n-k)))
