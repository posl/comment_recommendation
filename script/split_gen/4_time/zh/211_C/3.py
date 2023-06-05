def main():
    S = input()
    #S = "chokudaichokudaichokudai"
    #S = "chchokudai"
    #S = "atcoderrr"
    chokudai = "chokudai"
    #chokudai = "chchokudai"
    #chokudai = "atcoderrr"
    #chokudai = "chokudaichokudaichokudai"
    #chokudai = "chokudaichokudaichokudai"
    #chokudai = "chokudaichokudaichokudai"
    #chokudai = "chokudaichokudaichokudai"
    #chokudai = "chokudaichokudaichokudai"
    #chokudai = "chokudaichokudaichokudai"
    #chokudai = "chokudaichokudaichokudai"
    #chokudai = "chokudaichokudaichokudai"
    #chokudai = "chokudaichokudaichokudai"
    #print(S)
    #print(chokudai)
    #print(len(S))
    #print(len(chokudai))
    ans = 0
    for i in range(len(S)):
        if S[i] == chokudai[0]:
            for j in range(i+1, len(S)):
                if S[j] == chokudai[1]:
                    for k in range(j+1, len(S)):
                        if S[k] == chokudai[2]:
                            for l in range(k+1, len(S)):
                                if S[l] == chokudai[3]:
                                    for m in range(l+1, len(S)):
                                        if S[m] == chokudai[4]:
                                            for n in range(m+1, len(S)):
                                                if S[n] == chokudai[5]:
                                                    for o in range(n+1, len(S)):
                                                        if S[o] == chokudai[6]:
                                                            for p in range(o+1, len(S)):
                                                                if S[p] == chokudai[7]:
                                                                    ans += 1
                                                                    #print("ans", ans)
                                                                    #
