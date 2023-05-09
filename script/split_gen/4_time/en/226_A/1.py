def main():
    x = float(input())
    if x % 1 >= 0.5:
        print(int(x) + 1)
    else:
        print(int(x))
