def main():
    S = input()
    #print(S)
    #print(len(S))
    count = 0
    for i in range(len(S)):
        if S[i] == "c":
            for j in range(i+1,len(S)):
                if S[j] == "h":
                    for k in range(j+1,len(S)):
                        if S[k] == "o":
                            for l in range(k+1,len(S)):
                                if S[l] == "k":
                                    for m in range(l+1,len(S)):
                                        if S[m] == "u":
                                            for n in range(m+1,len(S)):
                                                if S[n] == "d":
                                                    for o in range(n+1,len(S)):
                                                        if S[o] == "a":
                                                            for p in range(o+1,len(S)):
                                                                if S[p] == "i":
                                                                    count += 1
    print(count)

if __name__ == '__main__':
    main()