def solve(h,w,coins):
    #先将偶数的单元格填满
    ans=[]
    for i in range(h):
        for j in range(w):
            if coins[i][j]%2==1:
                if j<w-1:
                    coins[i][j+1]+=1
                    ans.append((i+1,j+1,i+1,j+2))
                elif i<h-1:
                    coins[i+1][j]+=1
                    ans.append((i+1,j+1,i+2,j+1))
    #再将奇数的单元格填满
    for i in range(h):
        for j in range(w):
            while coins[i][j]%2==1:
                if j<w-1:
                    coins[i][j+1]+=1
                    ans.append((i+1,j+1,i+1,j+2))
                elif i<h-1:
                    coins[i+1][j]+=1
                    ans.append((i+1,j+1,i+2,j+1))
    return ans
