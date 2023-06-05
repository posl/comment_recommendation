def main():
    n,k = map(int,input().split())
    neta = []
    for i in range(n):
        t,d = map(int,input().split())
        neta.append([d,t])
    neta.sort(reverse=True)
    #print(neta)
    #print(neta[:k])
