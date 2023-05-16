def paint ( grid , x , y , color , visited ): # x, y is the current location # color is the color of the current location # visited is a set of visited locations # returns the number of sides of the polygon that has the current location as one of its vertices # if the current location is a black square, it returns 0 # if the current location is a white square, it returns 1 # if the current location is a black square and is adjacent to a white square, it returns 1 # if the current location is a white square and is adjacent to a black square, it returns 1 if grid [ y ][ x ] == '#' : return 0 if ( x , y ) in visited : return 0 visited . add (( x , y )) sides = 0 if x > 0 : sides += paint ( grid , x - 1 , y , color , visited ) if x < len ( grid [ y ]) - 1 : sides += paint ( grid , x + 1 , y , color , visited ) if y > 0 : sides += paint ( grid , x , y - 1 , color , visited ) if y < len ( grid ) - 1 : sides += paint ( grid , x , y + 1 , color , visited ) return sides

if __name__ == '__main__':
    paint()