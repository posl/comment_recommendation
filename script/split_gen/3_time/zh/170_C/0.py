def main():
    x,n = input().split()
    p = input().split()
    x = int(x)
    n = int(n)
    p = list(map(int,p))
    if n == 0:
        print(x)
        return
    p.append(x)
    p.sort()
    index = p.index(x)
    if index == 0:
        print(p[1])
    elif index == len(p)-1:
        print(p[-2])
    else:
        if p[index]-p[index-1] <= p[index+1]-p[index]:
            print(p[index-1])
        else:
            print(p[index+1])
