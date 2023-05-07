def   burger ( n ,   x ): 
     """ 
     Returns the number of patties in the bottom-most x layers from the bottom 
     of a level-n burger. 
     """ 
     if   n   ==   0 : 
         return   1 
     elif   x   ==   1 : 
         return   0 
     elif   x   <=   1   +   2 ** ( n   -   1 ): 
         return   burger ( n   -   1 ,   x   -   1 ) 
     else : 
         return   2 ** n   -   1   +   burger ( n   -   1 ,   x   -   2   -   2 ** ( n   -   1 ))
