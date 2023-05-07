def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        print(abs(X-A))
        return
    elif D > 0:
        # 0回以上の操作でXを良い数にする時、必要な操作の最小回数
        # 0回の操作でXを良い数にする場合
        # 1回以上の操作でXを良い数にする場合
        # 0回の操作でXを良い数にできる場合は、X-Aが最小の場合
        # 1回以上の操作でXを良い数にする場合は、X-AがDで割り切れる場合
        if (X-A) % D == 0:
            print(0)
            return
        else:
            print(min(abs((X-A) % D), abs(D-(X-A) % D)))
            return
    else:
        # D < 0の場合
        # 0回以上の操作でXを良い数にする時、必要な操作の最小回数
        # 0回の操作でXを良い数にする場合
        # 1回以上の操作でXを良い数にする場合
        # 0回の操作でXを良い数にできる場合は、X-Aが最小の場合
        # 1回以上の操作でXを良い数にする場合は、X-AがDで割り切れる場合
        if (X-A) % D == 0:
            print(0)
            return
        else:
            print(min(abs((X-A) % D), abs(D-(X-A) % D)))
            return
