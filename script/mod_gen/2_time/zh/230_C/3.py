def isSubString(T, S):
    index = 0
    for t in T:
        if t == S[index]:
            index += 1
        if index == len(S):
            return True
    return False

if __name__ == '__main__':
    isSubString()