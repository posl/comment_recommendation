def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    for i in range(1, b+1):
        if (a*i)%b == 0:
            print(a*i)
            break
