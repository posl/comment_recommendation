def f(x):
    #return sum([1 for i in range(1,x+1) if x%i==0])
    #return sum([1 for i in range(1,x+1) if x%i==0])
    return len([i for i in range(1,x+1) if x%i==0])
N = int(input())
print(sum([i*f(i) for i in range(1,N+1)]))
