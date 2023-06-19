def solve(n,s,w):
    #print(n,s,w)
    if n==1:
        if s[0]=="0":
            return 1
        else:
            return 0
    if n==2:
        if s[0]=="0" and s[1]=="0":
            return 2
        else:
            return 1
    if n==3:
        if s[0]=="0" and s[1]=="0" and s[2]=="0":
            return 3
        elif s[0]=="0" and s[1]=="0" and s[2]=="1":
            return 2
        elif s[0]=="0" and s[1]=="1" and s[2]=="0":
            return 2
        elif s[0]=="1" and s[1]=="0" and s[2]=="0":
            return 2
        else:
            return 1
    if n==4:
        if s[0]=="0" and s[1]=="0" and s[2]=="0" and s[3]=="0":
            return 4
        elif s[0]=="0" and s[1]=="0" and s[2]=="0" and s[3]=="1":
            return 3
        elif s[0]=="0" and s[1]=="0" and s[2]=="1" and s[3]=="0":
            return 3
        elif s[0]=="0" and s[1]=="1" and s[2]=="0" and s[3]=="0":
            return 3
        elif s[0]=="1" and s[1]=="0" and s[2]=="0" and s[3]=="0":
            return 3
        elif s[0]=="0" and s[1]=="0" and s[2]=="1" and s[3]=="1":
            return 2
        elif s[0]=="0" and s[1]=="1" and s[2]=="0" and s[3]=="1":
            return 2
        elif s[0]=="0" and s[1]=="1" and s[2]=="1" and s[3]=="0":
            return 2
        elif s[0]=="1" and s[1]=="0" and s[2]=="0" and s[3]=="

if __name__ == '__main__':
    solve()