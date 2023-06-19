Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    r, D, x = map(int, input().split())
    for i in range(10):
        x = r * x - D
        print(x)

=======
Suggestion 2

def f(r, D, x):
    for i in range(10):
        x = r * x - D
        print(x)

r, D, x = map(int, input().split())
f(r, D, x)

=======
Suggestion 3

def alg(r, d, x):
    for i in range(10):
        x = r * x - d
        print(x)

=======
Suggestion 4

def get_result(r, D, x_2000):
    x_2001 = r * x_2000 - D
    print(x_2001)
    for i in range(2, 11):
        x_2001 = r * x_2001 - D
        print(x_2001)

=======
Suggestion 5

def main():
    r,D,x_2000 = map(int,input().split())
    x_2001 = r*x_2000-D
    print(x_2001)
    x_2002 = r*x_2001-D
    print(x_2002)
    x_2003 = r*x_2002-D
    print(x_2003)
    x_2004 = r*x_2003-D
    print(x_2004)
    x_2005 = r*x_2004-D
    print(x_2005)
    x_2006 = r*x_2005-D
    print(x_2006)
    x_2007 = r*x_2006-D
    print(x_2007)
    x_2008 = r*x_2007-D
    print(x_2008)
    x_2009 = r*x_2008-D
    print(x_2009)
    x_2010 = r*x_2009-D
    print(x_2010)

=======
Suggestion 6

def fun(r, D, x):
    for i in range(10):
        x = r * x - D
        print(x)

=======
Suggestion 7

def main():
    r, D, x_2000 = map(int, input().split())
    for i in range(10):
        x_2000 = r * x_2000 - D
        print(x_2000)
