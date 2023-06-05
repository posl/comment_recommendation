def isSatisfy(strs):
    #print(strs)
    for i in range(len(strs)):
        if strs[i][0] == '!':
            if strs[i][1:] in strs:
                return strs[i][1:]
        else:
            if '!' + strs[i] in strs:
                return strs[i]
    return 'satisfy'
