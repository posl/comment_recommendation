def abc(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "A":
            for j in range(i+1,len(s)):
                if s[j] == "B":
                    for k in range(j+1,len(s)):
                        if s[k] == "C":
                            count += 1
    return count
