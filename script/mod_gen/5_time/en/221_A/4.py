def earthquake_energy():
    a,b = map(int, input().split())
    print(32**(a-b))
earthquake_energy()

if __name__ == '__main__':
    earthquake_energy()