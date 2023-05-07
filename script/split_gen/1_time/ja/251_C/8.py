def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    # まずは最も得点が高い提出を探す
    max_score = max(T)
    max_score_index = T.index(max_score)
    # 最も得点が高い提出の文字列を取得
    max_score_string = S[max_score_index]
    # 最も得点が高い提出よりも早い提出で、最も得点が高い提出と文字列が一致する提出を探す
    for i in range(max_score_index):
        if T[i] == max_score and S[i] == max_score_string:
            max_score_index = i
    print(max_score_index + 1)
