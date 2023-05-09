def main():
    x, y, r = map(float, input().split())
    r = int(r)
    #print(x, y, r)
    count = 0
    for i in range(r+1):
        for j in range(r+1):
            #print(i, j)
            if i**2 + j**2 <= r**2:
                count += 1
    print(count*4)
