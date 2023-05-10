def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    for i in range(n-1,0,-1):
        if h[i] < h[i-1]:
            h[i-1] -= 1
        elif h[i] > h[i-1]:
            print("No")
            return
    print("Yes")
