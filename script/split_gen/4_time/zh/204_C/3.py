def cal(N,M,city):
    result=0
    for i in range(N):
        for j in range(N):
            if i==j:
                result+=1
                continue
            flag=0
            for k in range(M):
                if city[k][0]==i+1 and city[k][1]==j+1:
                    flag=1
                    break
            if flag==0:
                result+=1
    return result
