def main():
    N,W = map(int,input().split())
    time = []
    for i in range(N):
        s,t,p = map(int,input().split())
        time.append([s,p])
        time.append([t,-p])
    time.sort()
    water = 0
    for i in range(2*N):
        water += time[i][1]
        if water > W:
            print("No")
            return
    print("Yes")
