def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(2001):
        if i not in A:
            print(i)
            break