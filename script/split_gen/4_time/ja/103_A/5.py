def main():
    #input
    a = list(map(int, input().split()))
    #compute
    a.sort()
    cost = a[2] - a[0] - a[1]
    #output
    print(cost)
