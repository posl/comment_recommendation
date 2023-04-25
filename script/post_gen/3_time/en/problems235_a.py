Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    abc = input()
    bca = abc[1] + abc[2] + abc[0]
    cab = abc[2] + abc[0] + abc[1]
    print(int(abc) + int(bca) + int(cab))

=======
Suggestion 2

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    bca = int(abc[1] + abc[2] + abc[0])
    cab = int(abc[2] + abc[0] + abc[1])
    print(a+b+c + bca + cab)

=======
Suggestion 3

def main():
    abc = int(input())
    a = abc // 100
    b = (abc % 100) // 10
    c = abc % 10
    bca = b * 100 + c * 10 + a
    cab = c * 100 + a * 10 + b
    print(abc + bca + cab)

=======
Suggestion 4

def main():
    abc = input()
    a = abc[0]
    b = abc[1]
    c = abc[2]
    print(int(a) + int(b) + int(c) + int(b) + int(c) + int(a) + int(c) + int(a) + int(b))

main()

=======
Suggestion 5

def main():
    abc = int(input())
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 10
    print(abc + b * 100 + c * 10 + a)

=======
Suggestion 6

def main():
    abc = int(input())
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 10
    print(a + b + c + b * 10 + c * 100 + a * 110)

=======
Suggestion 7

def main():
    abc = int(input())
    a = abc//100
    b = abc//10%10
    c = abc%10
    print(abc+b*100+c*10+a)

=======
Suggestion 8

def solve():
    abc = int(input())
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 10
    print(a+b+c+(b+c)*10+(c+a)*100)
    return

solve()

=======
Suggestion 9

def main():
    # Read the input
    abc = int(input())

    # Split the input into digits
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 10

    # Calculate the answer
    ans = a + b + c + a * 100 + b * 10 + c * 1

    # Print the answer
    print(ans)
