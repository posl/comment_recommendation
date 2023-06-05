def main():
    n,k,q = map(int,input().split())
    scores = [k]*n
    for i in range(q):
        scores[int(input())-1] += 1
    for i in range(n):
        if scores[i] <= q:
            print("No")
        else:
            print("Yes")
    return 0
