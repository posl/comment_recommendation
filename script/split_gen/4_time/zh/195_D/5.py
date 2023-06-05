def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    Query = []
    for i in range(Q):
        l, r = map(int, input().split())
        Query.append([l, r])
    for i in range(Q):
        l, r = Query[i]
        X_temp = X[:l-1] + X[r:]
        W_temp = W[:]
        V_temp = V[:]
        ans = 0
        for j in range(len(X_temp)):
            max_value = 0
            max_index = 0
            for k in range(len(W_temp)):
                if W_temp[k] <= X_temp[j] and V_temp[k] > max_value:
                    max_value = V_temp[k]
                    max_index = k
            if max_value > 0:
                ans += max_value
                W_temp.pop(max_index)
                V_temp.pop(max_index)
        print(ans)
