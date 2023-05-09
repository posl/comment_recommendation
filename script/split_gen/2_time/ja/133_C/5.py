def main():
    l,r = map(int,input().split())
    min = 2019
    for i in range(l,r):
        for j in range(i+1,r+1):
            if (i*j)%2019 < min:
                min = (i*j)%2019
    print(min)
