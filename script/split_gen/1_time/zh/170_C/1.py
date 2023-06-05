def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    if n == 0:
        print(x)
    else:
        p.append(x)
        p.sort()
        index = p.index(x)
        if index == 0:
            print(p[1])
        elif index == n:
            print(p[n-1])
        else:
            if (p[index] - p[index-1]) > (p[index+1] - p[index]):
                print(p[index+1])
            else:
                print(p[index-1])
