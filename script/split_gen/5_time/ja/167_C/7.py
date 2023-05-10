def check(books, n, m, x, c, a):
  #print("n,m,x,c,a", n,m,x,c,a)
  #print("books", books)
  #print("c", c)
  #print("a", a)
  #print("n", n)
  #print("m", m)
  #print("x", x)
  sum = 0
  for i in range(n):
    sum = sum + books[i] * c[i]
    #print("sum", sum)
  if sum >= x:
    return True
  else:
    return False
