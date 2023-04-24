Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = [input() for i in range(4)]
    if S.count("H") == 1 and S.count("2B") == 1 and S.count("3B") == 1 and S.count("HR") == 1:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    S = [input() for _ in range(4)]
    if "H" in S and "2B" in S and "3B" in S and "HR" in S:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    
    if s1 == 'H' and s2 == '2B' and s3 == '3B' and s4 == 'HR':
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def check(s):
    if s.count("H") == 1 and s.count("2B") == 1 and s.count("3B") == 1 and s.count("HR") == 1:
        return "Yes"
    else:
        return "No"

s = [input() for i in range(4)]
print(check(s))

=======
Suggestion 5

def main():
    S = [input() for _ in range(4)]
    S.sort()
    if S == ['2B', '3B', 'H', 'HR']:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def   main () : 
     s1   =   input () 
     s2   =   input () 
     s3   =   input () 
     s4   =   input () 

     if   ( s1   ==   'H'   or   s2   ==   'H'   or   s3   ==   'H'   or   s4   ==   'H' )   and   ( s1   ==   '2B'   or   s2   ==   '2B'   or   s3   ==   '2B'   or   s4   ==   '2B' )   and   ( s1   ==   '3B'   or   s2   ==   '3B'   or   s3   ==   '3B'   or   s4   ==   '3B' )   and   ( s1   ==   'HR'   or   s2   ==   'HR'   or   s3   ==   'HR'   or   s4   ==   'HR' ) : 
         print ( 'Yes' ) 
     else : 
         print ( 'No' )

=======
Suggestion 7

def main():
    s = set(input() for _ in range(4))
    if len(s) == 4:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = [input() for i in range(4)]
    if len(set(s)) == 4:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    S = [input() for _ in range(4)]
    print('Yes' if len(set(S)) == 4 else 'No')
