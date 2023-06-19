def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    x = 1
    while True:
        if x**3 >= N:
            break
        x += 1
    print(x**3)
