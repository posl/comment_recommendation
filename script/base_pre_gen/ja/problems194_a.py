#問題文
#日本において、アイス製品は次の 4 種類に大別されます。  
#乳固形分が 15 パーセント以上、乳脂肪分が 8 パーセント以上含まれるものを「アイスクリーム」とする。  
#上に当てはまらず、乳固形分が 10 パーセント以上、乳脂肪分が 3 パーセント以上含まれるものを「アイスミルク」とする。  
#上のいずれにも当てはまらず、乳固形分が 3 パーセント以上含まれるものを「ラクトアイス」とする。  
#上のいずれにも当てはまらないものを「氷菓」とする。  
#ここで、乳固形分は無脂乳固形分と乳脂肪分の 2 つから成ります。
#AtCoder 名物の製品「スヌケアイス」には、無脂乳固形分は A パーセント、乳脂肪分は B パーセント含まれています。
#スヌケアイスに上の分類を適用したとすると、4 種類のどれに当てはまるでしょうか ?
#答えは「出力」の項に従って整数で出力してください。  
#
#制約
#0 ≦ A ≦ 100
#0 ≦ B ≦ 100
#A + B ≦ 100
#A, B は整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#A B
#
#出力
#以下に定められる整数を出力せよ :
#スヌケアイスがアイスクリームに当てはまる場合 : 1
#スヌケアイスがアイスミルクに当てはまる場合 : 2
#スヌケアイスがラクトアイスに当てはまる場合 : 3
#スヌケアイスが氷菓に当てはまる場合 : 4
#
#入力例 1
#10 8
#
#出力例 1
#1
#このスヌケアイスには、無脂乳固形分が 10 パーセント、乳脂肪分が 8 パーセント含まれているため、乳固形分は 18 パーセント含まれています。
#乳固形分が 15 パーセント以上、乳脂肪分が 8 パーセント以上含まれているため、アイスクリームに分類されます。従って 1 が正しい出力です。  
#
#入力例 2
#1 2
#
#出力例 2
#3
#乳固形分がちょうど 3 パーセント含まれているため、アイスクリームやアイスミルクには該当しませんが、ラクトアイスに該当するため 3 を出力します。  
#
#入力例 3
#0 0
#
#出力例 3
#4
#氷菓に分類されます。  

def 