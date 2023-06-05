def main():
    a,b,w = map(int, input().split())
    w = w * 1000
    min = 1000000
    max = 0
    for i in range(1, w+1):
        if a <= i and i <= b:
            if w % i == 0:
                if min > w // i:
                    min = w // i
                if max < w // i:
                    max = w // i
    if max == 0:
        print("UNSATISFIABLE")
    else:
        print(str(min) + " " + str(max))
