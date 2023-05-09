def main():
    #n = int(input())
    #s = input()
    #a,b = map(int,input().split())
    n = int(input())
    s = [input() for _ in range(n)]
    #a = list(map(int,input().split()))
    #b = [list(map(int,input().split())) for _ in range(n)]
    #print(s)
    #print(a)
    #print(b)
    
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    #print(d)
    print(max(d, key=d.get))
