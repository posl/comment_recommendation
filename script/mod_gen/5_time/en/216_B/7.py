def isExistSameName(familyName, givenName, familyNameList, givenNameList):
    for i in range(0, len(familyNameList)):
        if familyName == familyNameList[i] and givenName == givenNameList[i]:
            return True
    return False
N = int(input())
familyNameList = []
givenNameList = []
for i in range(0, N):
    familyName, givenName = input().split(" ")
    familyNameList.append(familyName)
    givenNameList.append(givenName)
    if isExistSameName(familyName, givenName, familyNameList, givenNameList):
        print("Yes")
        exit()
print("No")

if __name__ == '__main__':
    isExistSameName()