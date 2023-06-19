def main():
    n = int(input())
    i = 1
    while True:
        print(i)
        x = int(input())
        if x == 0:
            break
        i = x
        if i >= 2 * n + 1:
            break
