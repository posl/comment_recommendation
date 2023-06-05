def main():
    h1, w1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(h2)]
    if h1 < h2 or w1 < w2:
        print("No")
        return
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            for k in range(h2):
                for l in range(w2):
                    if A[i+k][j+l] != B[k][l]:
                        break
                else:
                    continue
                break
            else:
                print("Yes")
                return
    print("No")
