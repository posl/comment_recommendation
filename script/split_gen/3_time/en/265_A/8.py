def main():
    X, Y, N = map(int, input().split())
    #print(X,Y,N)
    min_cost = N*X
    #print(min_cost)
    for i in range(0, N+1):
        #print(i)
        cost = i*X + (N-i)*Y//3
        #print(cost)
        if cost < min_cost:
            min_cost = cost
    print(min_cost)
