def main():
    A,B,C = (int(x) for x in input().split())
    if (A**2 + B**2) < C**2:
        print('Yes')
    else:
        print('No')
