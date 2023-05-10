def readinput():
    n,m=list(map(int,input().split()))
    x=list(map(int,input().split()))
    cy=[]
    for _ in range(m):
        c,y=list(map(int,input().split()))
        cy.append((c,y))
    return n,m,x,cy

if __name__ == '__main__':
    readinput()