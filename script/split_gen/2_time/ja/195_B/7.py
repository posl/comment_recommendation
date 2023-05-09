def main():
    A,B,W = map(int,input().split())
    W = W*1000
    max = W//A
    min = W//B
    if W%A != 0:
        min += 1
    if W%B != 0:
        max -= 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)
