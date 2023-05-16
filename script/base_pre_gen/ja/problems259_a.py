#問題文
#高橋君は N 歳の誕生日を迎えました。この時の彼の身長は T cmです。
#また、以下のことが分かっています。
#高橋君は 0 歳の誕生日(生まれた当日)から X 歳の誕生日までの間、毎年身長が D cmずつ伸びた。より厳密に書くと、i=1,2,...,X それぞれに対し、i-1 歳の誕生日から i 歳の誕生日までの間に身長が D cm伸びた。
#高橋君は X 歳の誕生日から N 歳の誕生日までの間、身長が変化していない。
#高橋君の M 歳の誕生日の時の身長が何cmだったかを求めてください。
#
#制約
#0 ≦ M < N ≦ 100
#1 ≦ X ≦ N
#1 ≦ T ≦ 200
#1 ≦ D ≦ 100
#高橋君の 0 歳の誕生日の時の身長は 1 cm以上である
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N M X T D
#
#出力
#答えを整数として出力せよ。
#
#入力例 1
#38 20 17 168 3
#
#出力例 1
#168
#この例では、高橋君の 38 歳の誕生日の時の身長が 168 cmです。また、17 歳の誕生日から 38 歳の誕生日までの間、身長が変化していません。
#このことから、20 歳の誕生日の時の身長は 168 cmだったと言え、これが答えになります。
#
#入力例 2
#1 0 1 3 2
#
#出力例 2
#1
#この例において、高橋君は 0(=M) 歳の誕生日の時の身長が 1 cmで、1(=N) 歳の誕生日の時の身長が 3(=T) cmです。
#
#入力例 3
#100 10 100 180 1
#
#出力例 3
#90

def 