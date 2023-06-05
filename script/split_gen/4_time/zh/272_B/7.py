def main():
    N,M = map(int,input().split())
    k = [0]*M
    x = [0]*M
    for i in range(M):
        k[i],x[i] = map(int,input().split())
    for i in range(M):
        for j in range(i+1,M):
            if len(set(x[i]) & set(x[j])) != 0:
                print("Yes")
                return
    print("No")
    return
