def main():
    a,b = map(int,input().split())
    if (a == 1 and b == 3) or (a == 1 and b == 4) or (a == 3 and b == 4) or (a == 2 and b == 3) or (a == 2 and b == 4) or (a == 2 and b == 5):
        print('Yes')
    else:
        print('No')
