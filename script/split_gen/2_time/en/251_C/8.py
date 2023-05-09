def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    # 1. 元の提出を抽出する
    # 2. 最高得点の提出を抽出する
    # 3. 最高得点の提出のうち、最も早い提出を抽出する
    # 4. 3の提出の番号を出力する
    # 1. 元の提出を抽出する
    original_submissions = []
    for i in range(N):
        # S[i] が S[:i] に存在するかどうか
        if S[i] not in S[:i]:
            original_submissions.append(i)
    # 2. 最高得点の提出を抽出する
    best_submissions = []
    best_score = -1
    for i in original_submissions:
        if T[i] > best_score:
            best_score = T[i]
    # 3. 最高得点の提出のうち、最も早い提出を抽出する
    best_submission = -1
    for i in original_submissions:
        if T[i] == best_score:
            best_submission = i
            break
    # 4. 3の提出の番号を出力する
    print(best_submission + 1)
