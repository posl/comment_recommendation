def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    # すぬけくんの番号をキー、初めて宝石を貰う時刻を値とする辞書を作成する。
    # すぬけくんは、初めに高橋くんから宝石を貰うので、
    # すぬけくんの初めて宝石を貰う時刻は、高橋くんから宝石を貰う時刻となる。
    # すぬけくんの初めて宝石を貰う時刻を初期値として、
    # すぬけくんの初めて宝石を貰う時刻を更新していく。
    # すぬけくんの初めて宝石を貰う時刻が、高橋くんから宝石を貰う時刻よりも後の場合は、
    # 高橋くんから宝石を貰う時刻を初めて宝石を貰う時刻とする。
    # すぬけくんの初めて宝石を貰う時刻が、高橋くんから宝石を貰う時刻よりも前の場合は、
    # すぬけくんの初めて宝石を貰う時刻をそのままとする。
    # すぬけくんの初めて宝石を貰う時刻が、高橋くんから宝石を貰う時刻と同じ場合は、
    # すぬけくんの初めて宝石を貰う時刻をそのままとする。
    # すぬけくんの初めて宝石を貰う
