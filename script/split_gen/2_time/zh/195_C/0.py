def main():
    a,b,w = map(int, input().split())
    min = 0
    max = 0
    for i in range(1,1000):
        if a*i <= w*1000 <= b*i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)
