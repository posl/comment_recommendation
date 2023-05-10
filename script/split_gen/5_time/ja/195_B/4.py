def main():
    a, b, w = map(int, input().split())
    w *= 1000
    max = 0
    min = 0
    for i in range(1, w+1):
        if a <= w/i <= b:
            if min == 0:
                min = i
            max = i
    if max == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)
