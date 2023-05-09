def main():
    X, A, D, N = map(int, input().split())
    # X が A + (N - 1) * D 以上の場合
    if X >= A + (N - 1) * D:
        print(X - (A + (N - 1) * D))
    # X が A + (N - 1) * D 以下の場合
    else:
        # X が A + (N - 2) * D 以上の場合
        if X >= A + (N - 2) * D:
            print(0)
        # X が A + (N - 2) * D 以下の場合
        else:
            print(min(abs(X - (A + (N - 2) * D)), abs(X - (A + (N - 1) * D))))
