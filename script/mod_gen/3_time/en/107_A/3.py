def findCar(n, i):
    return n-i+1
n, i = map(int, input().split())
print(findCar(n, i))

if __name__ == '__main__':
    findCar()