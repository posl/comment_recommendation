def getints(): return list(map(int, input().split()))
n,m=getints()
a=[]
for i in range(n):
    a.append(set(getints()[1:]))
print(len(set.intersection(*a)))

if __name__ == '__main__':
    getints()