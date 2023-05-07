def main():
    A,B,W = map(int, input().split())
    W *= 1000
    num_min = 0
    num_max = 0
    for i in range(1,1001):
        if A * i <= W <= B * i:
            num_min = i
            break
    for i in range(1000,0,-1):
        if A * i <= W <= B * i:
            num_max = i
            break
    if num_min == 0 and num_max == 0:
        print("UNSATISFIABLE")
    else:
        print(num_min,num_max)
