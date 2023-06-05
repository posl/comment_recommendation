def main():
    N = int(input())
    x = 1
    while True:
        if x * (x + 1) / 2 >= N:
            print(x)
            break
        else:
            x += 1
