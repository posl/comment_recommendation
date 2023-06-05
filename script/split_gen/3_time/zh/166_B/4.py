def main():
    n,k = map(int,input().split())
    #print(n,k)
    d = []
    for i in range(k):
        d.append(list(map(int,input().split())))
    #print(d)
    d = [item for sublist in d for item in sublist]
    #print(d)
    d = list(set(d))
    #print(d)
    print(n-len(d))
