#問題文
#1 以上 9 以下の数字のみからなる文字列 S が与えられます。
#この文字列の中で、あなたはこれら文字と文字の間のうち、いくつかの場所に + を入れることができます。
#一つも入れなくてもかまいません。
#ただし、+ が連続してはいけません。
#このようにして出来る全ての文字列を数式とみなし、和を計算することができます。
#ありうる全ての数式の値を計算し、その合計を出力してください。
#
#制約
#1 ≦ |S| ≦ 10
#S に含まれる文字は全て 1 〜 9 の数字
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#ありうる全ての数式の値の総和を 1 行に出力せよ。
#
#入力例 1
#125
#
#出力例 1
#176
#考えられる数式としては、 125、1+25、12+5、1+2+5 の 4 通りがあります。それぞれの数式を計算すると、
#125
#1+25=26
#12+5=17
#1+2+5=8
#となり、これらの総和は 125+26+17+8=176 となります。
#
#入力例 2
#9999999999
#
#出力例 2
#12656242944

def 