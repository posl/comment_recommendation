def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    max = 0
    for i in range(n):
        if h[i] >= max:
            max = h[i]
        else:
            break
    print(max)
