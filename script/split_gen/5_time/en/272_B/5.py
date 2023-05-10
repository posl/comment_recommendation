def main():
    N,M = map(int, input().split())
    x = []
    for i in range(M):
        x.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(i+1,N):
            if not (i+1 in x[j-i-1]):
                print("No")
                return
    print("Yes")
