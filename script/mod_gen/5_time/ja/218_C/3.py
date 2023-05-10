def check(s,t):
    for i in range(0,N):
        for j in range(0,N):
            if s[i][j] != t[i][j]:
                return False
    return True
N = int(input())
s = [input() for i in range(0,N)]
t = [input() for i in range(0,N)]
for i in range(0,N):
    s[i] = list(s[i])
    t[i] = list(t[i])
for i in range(0,4):
    for j in range(0,N):
        t[j] = t[j][::-1]
    t = list(map(list,zip(*t)))
    if check(s,t):
        print("Yes")
        exit()
print("No")

if __name__ == '__main__':
    check()