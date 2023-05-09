def main():
    n,s,d = map(int,input().split())
    spells = []
    for i in range(n):
        x,y = map(int,input().split())
        spells.append([x,y])
    for i in range(n):
        if spells[i][0]<s and spells[i][1]>d:
            print("Yes")
            exit()
    print("No")
