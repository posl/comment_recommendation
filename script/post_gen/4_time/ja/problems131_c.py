Synthesizing 1/10 solutions

=======
Suggestion 1

def main():
    A,B,C,D = map(int,input().split())
    #A以上B以下の整数のうち、CでもDでも割り切れないものの個数を求める
    #A以上B以下の整数の個数を求める
    #A以上B以下の整数の個数はB-A+1
    #CでもDでも割り切れるものの個数を求める
    #CでもDでも割り切れるものの個数は
    #Cで割り切れるものの個数はB//C-(A-1)//C
    #Dで割り切れるものの個数はB//D-(A-1)//D
    #CでもDでも割り切れるものの個数は
    #CとDの公倍数で割り切れるものの個数はB//(C*D)-(A-1)/
