#問題文
#Alice と Bob は、ロボットを制御するためのスイッチを1つずつ持っており、ロボットを動かしています。  
#Alice はロボットを動かし始めて A 秒後にスイッチを押し始め、ロボットを動かし始めて B 秒後にスイッチを離しました。  
#Bob はロボットを動かし始めて C 秒後にスイッチを押し始め、ロボットを動かし始めて D 秒後にスイッチを離しました。  
#Alice と Bob が、二人ともスイッチを押していた秒数を求めてください。   
#
#制約
#0≦A<B≦100
#0≦C<D≦100
#入力は全て整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。  
#A B C D
#
#出力
#Alice と Bob が二人ともスイッチを押していた秒数を出力せよ。   
#
#入力例 1
#0 75 25 100
#
#出力例 1
#50
#ロボットを動し始めて 0 秒後から 75 秒後までの間、Alice はスイッチを押していました。
#一方、ロボットを動し始めて 25 秒後から 100 秒後までの間、Bob はスイッチを押していました。
#したがって、二人が同時にスイッチを押していた時間は、ロボットを動し始めて 25 秒後から 75 秒後までの 50 秒です。
#
#入力例 2
#0 33 66 99
#
#出力例 2
#0
#Alice と Bob が同時にスイッチを押していないので、答えは 0 秒です。
#
#入力例 3
#10 90 20 80
#
#出力例 3
#60

def 