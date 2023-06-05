def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    cy = []
    for i in range(m):
        c,y = map(int,input().split())
        cy.append([c,y])
    cy.sort()
    cy.reverse()
    ans = 0
    for i in range(n):
        ans += x[i]
        for j in range(m):
            if cy[j][0] <= i+1:
                ans = max(ans,ans+cy[j][1])
    print(ans)
