def main():
    N,M,T = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    if AB[0][0] != 1:
        print("No")
        return
    for i in range(M-1):
        if AB[i][1] != AB[i+1][0]:
            print("No")
            return
    if AB[M-1][1] != T:
        print("No")
        return
    now = 0
    for i in range(M):
        now += AB[i][1]-AB[i][0]
    if now > N:
        print("No")
        return
    print("Yes")
