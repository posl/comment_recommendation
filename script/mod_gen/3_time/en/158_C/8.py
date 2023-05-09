def price(A,B):
    for i in range(1,1000):
        if B == int(i*0.1) and A == int(i*0.08):
            return i
    return -1
A,B = map(int,input().split())
print(price(A,B))

if __name__ == '__main__':
    price()