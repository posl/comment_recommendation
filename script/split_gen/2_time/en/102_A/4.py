def main():
    n = int(input())
    x = 1
    while x % n != 0:
        x = x * 2
    print(x)
