def  main():
     # 入力
      N  =  int (input())
     # 答え
      ans  =  0 
     # 桁数
      digit  =  1 
     # 10^digit
      ten  =  10 
     # 10^digit 以上 10^(digit+1) 未満の数の合計を計算
      while  ten  <=  N:
         # 桁数
          digit  +=  1 
         # 10^digit
          ten  *=  10 
         # 10^digit 以上 10^(digit+1) 未満の数の合計を計算
          ans  +=  9  *  10  **(digit  -   2 ) * digit
          ans  %=  998244353 
     # 10^digit 以上 N 未満の数の合計を計算
      ans  +=  (N  -   10  **(digit  -   1 ) +  1 ) * digit
      ans  %=  998244353 
     # 出力
      print (ans)

if __name__ == '__main__':
    ()