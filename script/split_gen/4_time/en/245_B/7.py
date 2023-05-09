def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = list(set(A))
    A.sort()
    for i in range(0, 2001):
        if i not in A:
            print(i)
            break
