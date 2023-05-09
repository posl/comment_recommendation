def main():
    a,b = map(int, input().split())
    if a > 0 and b > 0:
        print('Alloy')
    elif a > 0:
        print('Gold')
    else:
        print('Silver')
