def count(s):
    s = list(s)
    chokudaichokudaichokudai = list("chokudaichokudaichokudai")
    if len(s) < len(chokudaichokudaichokudai):
        return 0
    count = 0
    for i in range(len(s)):
        if s[i] == chokudaichokudaichokudai[0]:
            s[i] = ""
            for j in range(i+1, len(s)):
                if s[j] == chokudaichokudaichokudai[1]:
                    s[j] = ""
                    for k in range(j+1, len(s)):
                        if s[k] == chokudaichokudaichokudai[2]:
                            s[k] = ""
                            for l in range(k+1, len(s)):
                                if s[l] == chokudaichokudaichokudai[3]:
                                    s[l] = ""
                                    for m in range(l+1, len(s)):
                                        if s[m] == chokudaichokudaichokudai[4]:
                                            s[m] = ""
                                            for n in range(m+1, len(s)):
                                                if s[n] == chokudaichokudaichokudai[5]:
                                                    s[n] = ""
                                                    for o in range(n+1, len(s)):
                                                        if s[o] == chokudaichokudaichokudai[6]:
                                                            s[o] = ""
                                                            for p in range(o+1, len(s)):
                                                                if s[p] == chokudaichokudaichokudai[7]:
                                                                    s[p] = ""
                                                                    for q in range(p+1, len(s)):
                                                                        if s[q] == chokudaichokudaichokudai[8]:
                                                                            s[q] = ""
                                                                            for r in range(q+1, len(s)):
                                                                                if s[r] == chokudaichokudaichokudai[9]:
                                                                                    s[r] = ""
                                                                                    for t in range(r+1, len(s)):
                                                                                        if s[t] == chokudaichokudaichokudai[10]:
                                                                                            s[t] = ""
                                                                                            for u in range(t+1, len(s)):
                                                                                                if s[u] == chokudaichokudaichokudai[11]:
                                                                                                    s
