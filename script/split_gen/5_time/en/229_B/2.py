def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print('Easy')
    else:
        print('Hard')
