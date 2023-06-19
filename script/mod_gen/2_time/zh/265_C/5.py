def findway(h,w,grids):
    i=0
    j=0
    while(True):
        if grids[i][j]=="U":
            if i==0:
                return i,j
            else:
                i-=1
        elif grids[i][j]=="D":
            if i==h-1:
                return i,j
            else:
                i+=1
        elif grids[i][j]=="L":
            if j==0:
                return i,j
            else:
                j-=1
        elif grids[i][j]=="R":
            if j==w-1:
                return i,j
            else:
                j+=1
        else:
            return -1
        if i==0 and j==0:
            return i,j

if __name__ == '__main__':
    findway()