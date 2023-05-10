def main():
    a,b = map(int,input().split())
    if a == 0:
        print('Silver')
    elif b == 0:
        print('Gold')
    else:
        print('Alloy')
