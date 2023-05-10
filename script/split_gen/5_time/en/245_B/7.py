def main():
    N = int(input())
    A = list(map(int, input().split()))
    min = 0
    while True:
        if min in A:
            min += 1
        else:
            break
    print(min)
