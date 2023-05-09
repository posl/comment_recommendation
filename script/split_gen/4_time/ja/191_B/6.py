def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in A:
        if i == X:
            continue
        else:
            print(i, end=" ")
