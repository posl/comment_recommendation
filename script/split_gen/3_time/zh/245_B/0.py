def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 2002
    for i in a:
        b[i] += 1
    for i in range(2002):
        if b[i] == 0:
            print(i)
            break
