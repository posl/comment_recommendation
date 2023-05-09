def solve(w):
    if w%2 == 0:
        print(w//2)
        print(" ".join([str(i) for i in range(1, w//2+1)]))
    else:
        print(w//2+1)
        print(" ".join([str(i) for i in range(1, w//2+2)]))
w = int(input())
solve(w)
