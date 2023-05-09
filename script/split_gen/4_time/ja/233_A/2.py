def main():
    x,y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print(int((y-x)/10))
