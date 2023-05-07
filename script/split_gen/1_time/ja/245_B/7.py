def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(2010):
        if i in A:
            continue
        else:
            print(i)
            break
