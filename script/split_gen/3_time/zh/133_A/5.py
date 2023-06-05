def taxi_cost(n,a,b):
    return min(n*a,b)
n,a,b = map(int,input().split())
print(taxi_cost(n,a,b))
