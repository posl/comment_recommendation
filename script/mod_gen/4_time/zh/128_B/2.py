def getkey(item):
    return item[1]
N = int(input())
a = []
for i in range(N):
    s, p = input().split()
    a.append([i+1, s, int(p)])
a.sort(key=getkey, reverse=True)
a.sort(key=lambda x:x[1])
for i in range(N):
    print(a[i][0])

if __name__ == '__main__':
    getkey()