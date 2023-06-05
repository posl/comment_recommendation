def main():
    N = int(input())
    x = 0
    while N > 0:
        x += 1
        N -= x
    print(x)
