def count(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'c':
            for j in range(i+1,len(s)):
                if s[j] == 'h':
                    for k in range(j+1,len(s)):
                        if s[k] == 'o':
                            for l in range(k+1,len(s)):
                                if s[l] == 'k':
                                    for m in range(l+1,len(s)):
                                        if s[m] == 'u':
                                            for n in range(m+1,len(s)):
                                                if s[n] == 'd':
                                                    for o in range(n+1,len(s)):
                                                        if s[o] == 'a':
                                                            for p in range(o+1,len(s)):
                                                                if s[p] == 'i':
                                                                    count += 1
                                                                    #print(i,j,k,l,m,n,o,p)
    return count
