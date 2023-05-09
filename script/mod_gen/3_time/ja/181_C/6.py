def check(a,b,c):
    if(a[0] == b[0] and b[0] == c[0]):
        return True
    elif(a[1] == b[1] and b[1] == c[1]):
        return True
    elif(a[0] == b[0] and b[0] != c[0]):
        return False
    elif(a[1] == b[1] and b[1] != c[1]):
        return False
    else:
        if((a[1] - b[1])/(a[0] - b[0]) == (b[1] - c[1])/(b[0] - c[0])):
            return True
        else:
            return False
N = int(input())
xy = [list(map(int,input().split())) for i in range(N)]
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if(check(xy[i],xy[j],xy[k])):
                print('Yes')
                exit()
print('No')

if __name__ == '__main__':
    check()