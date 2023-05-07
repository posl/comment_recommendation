def main():
    N = int(input())
    A = list(map(int, input().split()))
    two = 0
    three = 0
    for i in A:
        while i % 2 == 0:
            two += 1
            i //= 2
        while i % 3 == 0:
            three += 1
            i //= 3
    if len(set(A)) == 1:
        print(abs(two - three))
    else:
        print(-1)
