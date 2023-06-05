def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(x)
    #print(n)
    #print(s)
    d = {}
    for i in range(len(x)):
        d[x[i]] = i
    #print(d)
    s.sort(key = lambda x: [d[c] for c in x])
    for i in s:
        print(i)

if __name__ == '__main__':
    main()