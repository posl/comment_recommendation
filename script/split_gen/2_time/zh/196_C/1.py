def solve():
    x = input()
    if '.' in x:
        x = x.split('.')[0]
    print(x)
