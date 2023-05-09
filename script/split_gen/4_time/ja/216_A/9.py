def main():
    x = float(input())
    y = int(x*10)%10
    if y <= 2:
        print(str(int(x))+'-')
    elif y <= 6:
        print(int(x))
    else:
        print(str(int(x))+'+')
