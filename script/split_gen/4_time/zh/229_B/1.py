def main():
    a, b = map(int, input().split())
    if a + b >= 10**10:
        print('Hard')
    else:
        print('Easy')
