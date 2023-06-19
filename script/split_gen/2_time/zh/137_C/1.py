def count(s):
    #print(s)
    s = list(s)
    s.sort()
    #print(s)
    count = 0
    c = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c += 1
        else:
            count += c*(c+1)/2
            c = 0
    count += c*(c+1)/2
    return count
n = int(input())
s = []
for i in range(n):
    s.append(input())
s.sort()
#print(s)
count = 0
c = 0
for i in range(n-1):
    if s[i] == s[i+1]:
        c += 1
    else:
        count += c*(c+1)/2
        c = 0
count += c*(c+1)/2
print(int(count))
