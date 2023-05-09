def   main ():
     n ,  x  =  map ( int ,  input (). split ())
     # The bottom-most X layers from the bottom of a level-N burger
     # can be described as the bottom-most X layers from the bottom
     # of a level-(N-1) burger, with the top bun removed, and
     # the bottom bun removed.
     # This is because the top bun and the bottom bun are not
     # part of the bottom-most X layers from the bottom of a
     # level-N burger.
     # Therefore, we can calculate the number of patties in the
     # bottom-most X layers from the bottom of a level-N burger
     # by recursively calling the function.
     print ( bottom_most_x_layers ( n ,  x ))

if __name__ == '__main__':
    ()