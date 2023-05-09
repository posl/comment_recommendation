def main():
    x, y, r = map(float, input().split())
    x, y = int(x*10000), int(y*10000)
    r = int(r*10000)
    #print(x,y,r)
    ans = 0
    for i in range(-r, r+1):
        if i*i > r*r:
            break
        j = int((r*r-i*i)**0.5)
        #print(i,j)
        while i*i+j*j > r*r:
            j -= 1
        ans += (y+j)//10000 - (y+i-1)//10000
        ans += (y-i)//10000 - (y-j-1)//10000
    print(ans)
