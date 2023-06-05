def main():
    n,k = map(int,input().split())
    s = input()
    s = [int(x) for x in s]
    if n==1:
        print(1)
        return
    if s[0]==0:
        s.insert(0,1)
    if s[-1]==0:
        s.append(1)
    if n==2:
        print(2)
        return
    s.insert(0,1)
    s.append(1)
    #print(s)
    l = 0
    r = 0
    max = 0
    while r<len(s)-1:
        if s[r+1]==0:
            if k>0:
                k -= 1
                r += 1
            else:
                if s[l]==0:
                    l += 1
                else:
                    l += 2
                    r += 1
        else:
            r += 1
        if r-l>max:
            max = r-l
    print(max)
    return
