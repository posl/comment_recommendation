def main():
    x,y,z = map(int, input().split())
    if x > y:
        print(x-z-y)
    else:
        print(-1)
