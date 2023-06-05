def main():
    N = int(input())
    x = 1
    while x*(x+1)/2 < N:
        x += 1
    print(x)
