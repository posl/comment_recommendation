def main():
    a,b,w = map(int,input().split())
    w *= 1000
    max_ = w // a
    min_ = w // b
    if w % b != 0:
        min_ += 1
    if min_ > max_:
        print("UNSATISFIABLE")
    else:
        print(min_, max_)
