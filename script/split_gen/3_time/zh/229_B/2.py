def main():
    a,b = map(int, input().split())
    if a+b < 10:
        print('Easy')
    else:
        print('Hard')
