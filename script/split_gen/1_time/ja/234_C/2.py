def main():
    K = int(input())
    # 0,2のみからなる正整数を小さい方から並べると、2,20,22,200,202,220,222,...となる
    # つまり、2**i個の0,2のみからなる正整数が2**(i+1)個ある
    # この正整数は、2**(i+1)個の0,2のみからなる正整数のうち、2**i個目の正整数から2**(i+1)個目の正整数までの間にある
    # つまり、2**(i+1)個の0,2のみからなる正整数のうち、2**i個目の正整数から2**(i+1)個目の正整数までの間にあるものがK個目
    # ということで、K個目の正整数を2進数で表したときに、2**(i+1)桁の0,2のみからなる正整数になる
    # この正整数を求める
    # この正整数を求めるには、Kを2進数に変換して、0,2のみからなる正整数を作る
    # つまり、Kを2進数に変換して、0,2のみからなる正整数を作る
    # 0,2のみからなる正整数を作るには、0,2のみからなる正整数を作る
    # 0,2のみからなる正整数を作るには、0,2のみからなる正整数を作る
    # ということで、再帰関数を使う
    # また、0,2のみからなる正整数を作るには、0,2のみからなる正整数を作る
    # 0,2のみからな
