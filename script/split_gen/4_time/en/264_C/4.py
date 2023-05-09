def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for i in range(h2)]
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            for k in range(h2):
                if a[i + k][j:j + w2] != b[k]:
                    break
            else:
                print('Yes')
                return
    print('No')
