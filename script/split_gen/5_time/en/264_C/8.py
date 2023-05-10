def main():
    h1, w1 = map(int, input().split())
    a = [[0 for i in range(w1)] for j in range(h1)]
    for i in range(h1):
        a[i] = list(map(int, input().split()))
    h2, w2 = map(int, input().split())
    b = [[0 for i in range(w2)] for j in range(h2)]
    for i in range(h2):
        b[i] = list(map(int, input().split()))
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if a[i][j] == b[0][0]:
                if a[i:i + h2] == b:
                    print("Yes")
                    return
    print("No")
