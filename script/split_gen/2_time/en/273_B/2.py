def main():
    x,k = map(int, input().split())
    for i in range(k):
        if x % 10 == 0:
            x /= 10
        else:
            x -= 1
    print(int(x))
