def main():
    a,b,w = map(int,input().split())
    w = w * 1000
    min = w // b
    max = w // a
    if w % b != 0:
        min += 1
    if w % a != 0:
        max -= 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)
