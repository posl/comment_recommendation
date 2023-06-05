def main():
    #n = int(input())
    #a = [0]*n
    #for i in range(n):
    #    a[i] = int(input())
    #a.sort()
    #print(a[-1]-a[0])
    #print(a)
    #print(a[-1])
    #print(a[0])
    q = int(input())
    a = []
    for i in range(q):
        query = input()
        if query[0] == "1":
            a.append(int(query.split()[1]))
        elif query[0] == "2":
            x, c = map(int, query.split()[1:])
            for j in range(min(c, a.count(x))):
                a.remove(x)
        else:
            a.sort()
            print(a[-1]-a[0])
