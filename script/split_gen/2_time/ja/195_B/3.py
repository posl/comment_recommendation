def main():
    A,B,W = map(int,input().split())
    W *= 1000
    min = W // B
    max = W // A
    if W % B != 0:
        min += 1
    if W % A != 0:
        max -= 1
    if max < min:
        print("UNSATISFIABLE")
    else:
        print(min,max)
