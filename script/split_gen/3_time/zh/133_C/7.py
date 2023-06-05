def main():
    l,r = list(map(int,input().split()))
    if l == r:
        print(0)
    elif r-l >= 2019:
        print(0)
    else:
        min = 2019
        for i in range(l,r):
            for j in range(i+1,r+1):
                if (i*j)%2019 < min:
                    min = (i*j)%2019
        print(min)
