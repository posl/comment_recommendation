def problems243_a():
    v,a,b,c = map(int, input().split())
    if v % a == 0 or v % b == 0 or v % c == 0:
        print("T")
    else:
        print("F")
