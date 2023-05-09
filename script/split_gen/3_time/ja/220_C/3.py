def main():
    n = int(input())
    a = list(map(int,input().split()))
    x = int(input())
    b = a * 100
    bsum = 0
    for i in range(len(b)):
        bsum += b[i]
        if bsum > x:
            print(i+1)
            break
