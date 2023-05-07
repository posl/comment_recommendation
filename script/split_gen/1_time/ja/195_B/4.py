def main():
    a,b,w = map(int,input().split())
    w *= 1000
    max = w//a
    min = w//b
    if w%b != 0:
        min += 1
    if max < min:
        print("UNSATISFIABLE")
    else:
        print(min,max)
