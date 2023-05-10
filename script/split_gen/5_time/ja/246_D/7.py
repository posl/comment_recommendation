def main():
    n = int(input())
    x = 0
    if n == 0:
        print(0)
        return
    for i in range(100):
        if n <= (i+1)**4:
            x = i+1
            break
    #print(x)
    for i in range(x+1):
        for j in range(x+1):
            if i**3+i**2*j+i*j**2+j**3 == n:
                print(i**3+i**2*j+i*j**2+j**3)
                return
