def main():
    x,y = map(int,input().split())
    if x >= y:
        print(0)
    else:
        print(y//10 - x//10)
