def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = int(w/b)
    max = int(w/a)
    if w%b != 0:
        min += 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)
