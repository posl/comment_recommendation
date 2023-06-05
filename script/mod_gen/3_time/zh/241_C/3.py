def check(i,j):
    if 0<=i<=n-6 and 0<=j<=n-6:
        for k in range(6):
            if s[i+k][j+k]==".":
                return False
        return True
    return False
n=int(input())
s=[]
for i in range(n):
    s.append(input())
for i in range(n):
    for j in range(n):
        if s[i][j]==".":
            s[i]=s[i][:j]+"#"+s[i][j+1:]
            if check(i,j):
                print("Yes")
                exit()
            s[i]=s[i][:j]+"."+s[i][j+1:]
print("No")

if __name__ == '__main__':
    check()