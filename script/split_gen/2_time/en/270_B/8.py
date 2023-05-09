def main():
    x,y,z = map(int, input().split())
    if x < y < z:
        print(z - x)
    else:
        print(-1)
