def cutbar(m,n,current):
    if current >= n: #如果当前长度大于等于n，返回0
        return 0
    elif current < m: #如果当前长度小于m，返回1+cutbar(m,n,current*2)，因为当前长度小于m，所以剩下的长度大于m，所以需要再切一刀，长度变为原来的两倍
        return 1+cutbar(m,n,current*2)
    else: #如果当前长度大于等于m，返回1+cutbar(m,n,current+m)，因为当前长度大于等于m，所以剩下的长度大于等于m，所以需要再切一刀，长度变为原来的m
        return 1+cutbar(m,n,current+m)
    
print(cutbar(3,20,1))
print(cutbar(5,100,1))
print(cutbar(12,200,1))
