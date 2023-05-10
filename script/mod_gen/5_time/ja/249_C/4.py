def main():
    n,k = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())
    s.sort()
    #print(s)
    ans = 0
    for i in range(2**n):
        t = []
        for j in range(n):
            if ((i>>j)&1):
                t.append(s[j])
        #print(t)
        if len(t) == 0:
            continue
        if len(t) > k:
            continue
        if len(t) == k:
            #print(t)
            temp = []
            for x in t:
                for y in x:
                    temp.append(y)
            #print(temp)
            temp.sort()
            #print(temp)
            count = 0
            for x in range(len(temp)-1):
                if temp[x] == temp[x+1]:
                    count += 1
            if count == k:
                ans = max(ans, len(set(temp)))
    print(ans)

if __name__ == '__main__':
    main()