def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a_ = []
    for i in range(n):
        if a[i] != x:
            a_.append(a[i])
    for i in range(len(a_)):
        print(a_[i], end=" ")
    print()
