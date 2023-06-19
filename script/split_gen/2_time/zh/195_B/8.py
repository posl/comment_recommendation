def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = (w//b) if w%b == 0 else (w//b)+1
    max = w//a
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)
