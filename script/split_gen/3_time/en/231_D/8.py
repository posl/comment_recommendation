def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for i in range(M)]
    AB.sort(key=lambda x:x[0])
    AB.sort(key=lambda x:x[1])
    ans = "Yes"
    for i in range(M-1):
        if AB[i][1] == AB[i+1][1]:
            ans = "No"
            break
    print(ans)
