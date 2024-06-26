#問題文
#相異なる二つの文字列 S, T が与えられます。
#S が T よりも辞書順で小さい場合は Yes を、大きい場合は No を出力してください。
#辞書順とは？
#辞書順とは簡単に説明すると「単語が辞書に載っている順番」を意味します。より厳密な説明として、相異なる文字列 S と文字列 T の大小を判定するアルゴリズムを以下に説明します。
#以下では「 S の i 文字目の文字」を S_i のように表します。また、 S が T より辞書順で小さい場合は S < T 、大きい場合は S > T と表します。
# S と T のうち長さが短い方の文字列の長さを L とします。i=1,2,...,L に対して S_i と T_i が一致するか調べます。 
# S_i ≠ T_i である i が存在する場合、そのような i のうち最小のものを j とします。そして、S_j と T_j を比較して、 S_j がアルファベット順で T_j より小さい場合は S < T 、大きい場合は S > T と決定して、アルゴリズムを終了します。
#  
# S_i ≠ T_i である i が存在しない場合、 S と T の長さを比較して、S が T より短い場合は S < T 、長い場合は S > T と決定して、アルゴリズムを終了します。 
#なお、主要なプログラミング言語の多くでは、文字列の辞書順による比較は標準ライブラリに含まれる関数や演算子として実装されています。詳しくは各言語のリファレンスをご参照ください。
#
#制約
#S, T は英小文字からなる長さ 1 以上 10 以下の相異なる文字列である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S T
#
#出力
#S が T より辞書順で小さい場合は Yes を、大きい場合は No を出力せよ。
#
#入力例 1
#abc atcoder
#
#出力例 1
#Yes
#abc と atcoder は 1 文字目が同じで 2 文字目が異なります。 アルファベットの b は t よりもアルファベット順で先に来るので、 abc の方が atcoder よりも辞書順で小さいことがわかります。
#
#入力例 2
#arc agc
#
#出力例 2
#No
#
#入力例 3
#a aa
#
#出力例 3
#Yes

def 