def main():
    k, x = map(int, input().split())
    max = 1000000
    min = -1000000
    if x + k > max:
        max = x + k
    if x - k < min:
        min = x - k
    for i in range(min, max+1):
        print(i, end=" ")
