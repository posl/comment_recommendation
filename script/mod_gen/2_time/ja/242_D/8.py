def main():
    S = input()
    Q = int(input())
    query = []
    for i in range(Q):
        t,k = map(int,input().split())
        query.append([t,k])
    
    #Sの各文字をA→BC,B→CA,C→ABと置き換える
    #A→BC,B→CA,C→AB
    #A→B,B→C,C→A
    #A→1,B→2,C→3
    #1→B,2→C,

if __name__ == '__main__':
    main()