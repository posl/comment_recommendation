def main():
    n, m, x, y = map(int, input().split())
    xa = set(map(int, input().split()))
    ya = set(map(int, input().split()))
    for z in range(x+1, y+1):
        if z not in xa and z not in ya:
            print('No War')
            exit()
    print('War')
