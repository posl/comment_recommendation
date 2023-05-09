def problems278_a():
    #input
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    #calculate
    for i in range(k):
        a.pop(0)
        a.append(0)
    #output
    print(*a)

if __name__ == '__main__':
    problems278_a()