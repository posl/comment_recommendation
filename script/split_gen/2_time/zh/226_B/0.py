def main():
    x = float(input())
    if x < 0 or x >= 100:
        return
    y = x * 10
    if y % 10 >= 5:
        print(int(x) + 1)
    else:
        print(int(x))
