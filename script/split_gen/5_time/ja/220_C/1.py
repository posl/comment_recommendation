def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    b = a * (10**100)
    sum = 0
    for i in range(len(b)):
        sum += b[i]
        if sum > x:
            print(i+1)
            break
