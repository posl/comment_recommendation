def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(n-1):
        if h[i] < h[i+1]:
            count = 0
        else:
            count += 1
        if count > max:
            max = count
    print(h[max])
