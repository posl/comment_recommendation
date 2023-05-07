def isSmaller(s1,s2):
    if s1<s2:
        return "Yes"
    else:
        return "No"
s1,s2 = input().split()
print(isSmaller(s1,s2))

if __name__ == '__main__':
    isSmaller()