def main():
    n = int(input())
    judge = 1
    while judge == 1:
        print(1)
        x = int(input())
        if x == 0:
            judge = 0
        else:
            print(2 * n + 1 - x)
            y = int(input())
            if y == 0:
                judge = 0
