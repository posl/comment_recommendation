def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2^N人の選手の中で、最もレートの高い選手の番号を求める
    max_player = A.index(max(A)) + 1
    # 2^N人の選手の中で、最もレートの高い選手以外の中で、最もレートの高い選手の番号を求める
    A[max_player - 1] = 0
    second_max_player = A.index(max(A)) + 1
    print(second_max_player)
