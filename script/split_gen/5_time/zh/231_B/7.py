def main():
    #input
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #process
    s.sort()
    c = {}
    for i in range(n):
        if s[i] in c:
            c[s[i]] += 1
        else:
            c[s[i]] = 1
    #output
    print(max(c, key=c.get))
