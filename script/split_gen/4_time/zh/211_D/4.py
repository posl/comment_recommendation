def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    AB = sorted(AB,key=lambda x:x[1])
    #print(AB)
    city = 1
    count = 0
    for a,b in AB:
        if a == city:
            city = b
            count += 1
    print(count)
main()
