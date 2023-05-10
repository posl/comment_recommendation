def main():
    x = float(input())
    if x < 0.5:
        print(0)
    elif x < 100:
        print(int(x)+1)
    else:
        print(100)
