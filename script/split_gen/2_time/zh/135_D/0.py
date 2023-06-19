def solve(s):
    #print("s={}".format(s))
    #print("len(s)={}".format(len(s)))
    if len(s) == 0:
        return 0
    if len(s) == 1:
        if s[0] == '?':
            return 0
        if int(s[0]) % 13 == 5:
            return 1
        else:
            return 0
    if s[0] == '?':
        #print("s[0] == '?'")
        #print("solve(s[1:])={}".format(solve(s[1:])))
        return 10 * solve(s[1:])
    else:
        #print("s[0] != '?'")
        #print("solve(s[1:])={}".format(solve(s[1:])))
        return solve(s[1:])
