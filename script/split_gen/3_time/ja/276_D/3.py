def main():
    N = int(input())
    A = list(map(int, input().split()))
    two = 0
    three = 0
    for a in A:
        while a % 2 == 0:
            a //= 2
            two += 1
        while a % 3 == 0:
            a //= 3
            three += 1
        if a != 1:
            print(-1)
            return
    print(two + three)
