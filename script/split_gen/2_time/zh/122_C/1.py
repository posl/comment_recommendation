def main():
    n,q = map(int,input().split())
    s = input()
    l = []
    for i in range(q):
        l.append(list(map(int,input().split())))
    
    for i in range(q):
        print(s.count('AC',l[i][0]-1,l[i][1]))
