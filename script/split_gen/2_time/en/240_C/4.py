def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    sum = 0
    for i in range(N):
        if X < a[i]:
            sum += a[i]
        else:
            sum += b[i]
    if sum <= X:
        print("Yes")
    else:
        print("No")
