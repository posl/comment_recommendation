def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(1, w + 1):
        if a <= i <= b:
            if w % i == 0:
                min = i
                max = i
            elif w % i != 0:
                if min == 0:
                    min = i
                max = i
    if min == 0 and max == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)
