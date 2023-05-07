def  main():
     # 文字列を取得する 
     s  =  input()
     # 文字列の長さを取得する 
     n  =  len(s)
     # 各文字の出現回数を数える 
     c  =  [ 0 ] *  26 
     for  i  in  range(n):
        c[ord(s[i]) -  ord ( 'a' )] +=  1 
     # 文字列の中に必要な文字が含まれているかを確認する 
     if  c[ 2 ] <  1   or  c[ 7 ] <  1   or  c[ 14 ] <  1   or  c[ 10 ] <  1   or  c[ 20 ] <  1   or  c[ 3 ] <  1   or  c[ 0 ] <  1   or  c[ 8 ] <  1 :
         # 必要な文字が含まれていない場合は 0 を出力する 
         print ( 0 )
         return 
     # 各文字の出現回数を 1 減らす

if __name__ == '__main__':
    ()