def main():
    # input
    a,b = map(int, input().split())
    # check
    if a+b < 10**10:
        print('Easy')
    else:
        print('Hard')
