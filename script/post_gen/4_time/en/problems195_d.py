Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    L = []
    R = []
    for i in range(Q):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    for i in range(Q):
        X_ = X[:L[i]-1] + X[R[i]:]
        X_.sort()
        ans = 0
        for j in range(N):
            for k in range(M-1, -1, -1):
                if W[j] <= X_[k]:
                    ans += V[j]
                    X_.pop(k)
                    break
        print(ans)
    return

main()

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        X_copy = X.copy()
        del X_copy[L-1:R]
        X_copy.sort()
        baggages = []
        for x in X_copy:
            baggages.append((x, -1))
        for i in range(N):
            baggages.append((W[i], V[i]))
        baggages.sort(reverse=True)
        used = [False] * N
        ans = 0
        for x, v in baggages:
            for i in range(N):
                if not used[i] and W[i] <= x:
                    used[i] = True
                    ans += v
                    break
        print(ans)

=======
Suggestion 3

def solve():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        X_copy = X[:L-1] + X[R:]
        X_copy.sort()
        ans = 0
        for i in range(N):
            for j in range(len(X_copy)):
                if W[i] <= X_copy[j]:
                    ans += V[i]
                    X_copy.pop(j)
                    break
        print(ans)

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    LR = [list(map(int, input().split())) for _ in range(Q)]

    WV.sort(key=lambda x: x[1], reverse=True)

    for l, r in LR:
        x = X[:l-1] + X[r:]
        x.sort()
        ans = 0
        for w, v in WV:
            for i, xi in enumerate(x):
                if w <= xi:
                    ans += v
                    x.pop(i)
                    break
        print(ans)

=======
Suggestion 5

def solve():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    LR = [list(map(int, input().split())) for _ in range(Q)]

    WV.sort(key=lambda x: x[1], reverse=True)
    for l, r in LR:
        boxes = X[:l-1] + X[r:]
        boxes.sort()
        used = [False] * (N+1)
        ans = 0
        for box in boxes:
            for i in range(N):
                if not used[i] and WV[i][0] <= box:
                    used[i] = True
                    ans += WV[i][1]
                    break
        print(ans)

=======
Suggestion 6

def solve():
    N, M, Q = map(int, input().split())
    WV = [tuple(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    WV.sort(key=lambda wv: wv[1], reverse=True)
    X.sort(reverse=True)

    for L, R in queries:
        boxes = X[:L-1] + X[R:]
        boxes.sort(reverse=True)

        ans = 0
        for w, v in WV:
            for i, box in enumerate(boxes):
                if w <= box:
                    ans += v
                    del boxes[i]
                    break

        print(ans)

=======
Suggestion 7

def get_max_value(baggage, boxes):
    max_value = 0
    for bag in baggage:
        for box in boxes:
            if box[1] >= bag[0]:
                if box[0] > max_value:
                    max_value = box[0]
    return max_value

=======
Suggestion 8

def solve(baggage, box, query):
    box.sort()
    for i in range(len(query)):
        l, r = query[i]
        temp = box[:l-1] + box[r:]
        temp.sort()
        box_size = [x[0] for x in temp]
        box_value = [x[1] for x in temp]
        #print(box_size, box_value)
        res = 0
        for j in range(len(baggage)):
            for k in range(len(box_size)):
                if baggage[j][0] <= box_size[k]:
                    res += box_value[k]
                    box_size.pop(k)
                    box_value.pop(k)
                    break
        print(res)
    return

=======
Suggestion 9

def get_max_value_baggage(baggage, boxes):
    #sort by weight so that we can use binary search
    baggage = sorted(baggage, key=lambda x: x[0])
    boxes = sorted(boxes)
    #dp[i][j] is the maximum value we can get by using the first i baggage and j boxes
    dp = [[0 for _ in range(len(boxes) + 1)] for _ in range(len(baggage) + 1)]
    for i in range(1, len(baggage) + 1):
        for j in range(1, len(boxes) + 1):
            #if the current box can hold the current baggage
            if boxes[j - 1] >= baggage[i - 1][0]:
                #we can either put the current baggage in the current box or not
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + baggage[i - 1][1])
            else:
                #we can't put the current baggage in the current box
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]

=======
Suggestion 10

def input():
    return sys.stdin.readline().rstrip()
