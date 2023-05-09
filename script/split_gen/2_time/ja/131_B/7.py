def main():
    N, L = map(int, input().split())
    # 全て食べる場合のアップルパイの味
    all = sum([L+i-1 for i in range(1, N+1)])
    # 一番味の悪いリンゴを食べない場合のアップルパイの味
    not_eat = sum([L+i-1 for i in range(1, N+1) if i != N])
    # 一番味の悪いリンゴを食べる場合のアップルパイの味
    eat = sum([L+i-1 for i in range(1, N+1) if i != 1])
    # 一番味の悪いリンゴを食べない場合と食べる場合のうちどちらがアップルパイの味が近いかで場合分け
    if abs(all - not_eat) < abs(all - eat):
        print(not_eat)
    else:
        print(eat)
