def earthquake():
    a,b = map(int,input().split())
    return 32**(a-b)
print(earthquake())

if __name__ == '__main__':
    earthquake()