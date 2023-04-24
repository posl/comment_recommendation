Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = input()
    n = n.replace('1','2')
    n = n.replace('9','1')
    n = n.replace('2','9')
    print(n)

=======
Suggestion 2

def main():
    n = input()
    print(n.replace('1', 'x').replace('9', '1').replace('x', '9'))

=======
Suggestion 3

def main():
    n = input()
    n = n.replace("1","x")
    n = n.replace("9","1")
    n = n.replace("x","9")
    print(n)

main()

=======
Suggestion 4

def main():
    n = input()
    print(n.replace('1', 'A').replace('9', '1').replace('A', '9'))

=======
Suggestion 5

def solution():
    n = input()
    result = n.replace('1', 'x')
    result = result.replace('9', '1')
    result = result.replace('x', '9')
    print(result)

solution()

=======
Suggestion 6

def main():
    n = input()
    print(n.replace("1","x").replace("9","1").replace("x","9"))
    return

=======
Suggestion 7

def main():
    n = input()
    print(n.replace('1','x').replace('9','1').replace('x','9'))
main()

=======
Suggestion 8

def swap(n):
    return n.replace('1', 'x').replace('9', '1').replace('x', '9')

n = input()
print(swap(n))

=======
Suggestion 9

def problems111_a():
    n = input()
    print(n.translate(str.maketrans('19','91')))
    return
