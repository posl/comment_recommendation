def main():
    n, m = map(int, input().split())
    l = []
    for i in range(m):
        l.append(list(map(int, input().split()))[1:])
    for i in range(m):
        for j in range(i+1, m):
            if len(set(l[i]+l[j])) == len(l[i])+len(l[j]):
                print("NO")
                return
    print("YES")
