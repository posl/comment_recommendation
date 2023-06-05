def findAB(x):
    for i in range(-1000,1000):
        for j in range(-1000,1000):
            if i**5-j**5 == x:
                return i,j
    return 0,0
x = int(input())
a,b = findAB(x)
print(a,b)

if __name__ == '__main__':
    findAB()