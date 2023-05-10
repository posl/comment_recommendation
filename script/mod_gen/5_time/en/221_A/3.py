def earthquake():
    A, B = map(int, input().split())
    print(32**(A-B))
earthquake()

if __name__ == '__main__':
    earthquake()