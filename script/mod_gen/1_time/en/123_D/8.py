def main():
    X,Y,Z,K=map(int, input().split())
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))
    C=list(map(int, input().split()))
    AB=[]
    for a in A:
        for b in B:
            AB.append(a+b)
    AB.sort()
    AB.reverse()
    ABC=[]
    for i in range(min(K,len(AB))):
        for c in C:
            ABC.append(AB[i]+c)
    ABC.sort()
    ABC.reverse()
    for i in range(K):
        print(ABC[i])

if __name__ == '__main__':
    main()