def get_max_sum_of_cake(n,m,beauty,deliciousness,popularity):
    max_sum=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                sum=abs(beauty[i])+abs(beauty[j])+abs(beauty[k])
                sum+=abs(deliciousness[i])+abs(deliciousness[j])+abs(deliciousness[k])
                sum+=abs(popularity[i])+abs(popularity[j])+abs(popularity[k])
                max_sum=max(max_sum,sum)
    return max_sum
