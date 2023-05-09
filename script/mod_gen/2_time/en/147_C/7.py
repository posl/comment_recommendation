def check ( honest , testimony , n ) : for i in range ( n ) : if honest [ i ] == 1 : for ( x , y ) in testimony [ i ] : if y == 1 : if honest [ x - 1 ] == 0 : return False else : if honest [ x - 1 ] == 1 : return False return True

if __name__ == '__main__':
    check()