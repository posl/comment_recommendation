def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    for i in range(2001):
        if i not in A:
            print(i)
            break
