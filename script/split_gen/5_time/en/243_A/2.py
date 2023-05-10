def main():
    v, a, b, c = map(int, input().split())
    shampoo = [a, b, c]
    while v > 0:
        for i in range(3):
            v -= shampoo[i]
            if v < 0:
                if i == 0:
                    print("F")
                elif i == 1:
                    print("M")
                else:
                    print("T")
                return 0
