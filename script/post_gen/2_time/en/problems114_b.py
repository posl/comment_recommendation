Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    ans = 753
    for i in range(len(S)-2):
        ans = min(ans, abs(753 - int(S[i:i+3])))
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    ans = 1000
    for i in range(len(s)-2):
        ans = min(ans, abs(753 - int(s[i:i+3])))
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    min = 753
    for i in range(len(s) - 2):
        if abs(int(s[i:i+3]) - 753) < min:
            min = abs(int(s[i:i+3]) - 753)
    print(min)

main()

=======
Suggestion 4

def main():
    S = input()
    print(min([abs(int(S[i:i + 3]) - 753) for i in range(len(S) - 2)]))

=======
Suggestion 5

def main():
    s = input()
    min = 1000
    for i in range(len(s) - 2):
        n = int(s[i:i+3])
        if abs(753 - n) < min:
            min = abs(753 - n)
    print(min)

=======
Suggestion 6

def main():
    S = input()
    min_diff = 1000
    for i in range(len(S)-2):
        num = int(S[i:i+3])
        if abs(num-753) < min_diff:
            min_diff = abs(num-753)
    print(min_diff)

=======
Suggestion 7

def main():
    s = input()
    s = [int(i) for i in s]
    answer = 753
    for i in range(len(s)-2):
        if answer > abs(753 - int(s[i] * 100 + s[i+1] * 10 + s[i+2])):
            answer = abs(753 - int(s[i] * 100 + s[i+1] * 10 + s[i+2]))
    print(answer)

=======
Suggestion 8

def main():
    S = input()

    #Initialize the minimum difference to be 753
    min_diff = 753

    #Loop through the string S to find the minimum difference between 753 and the integer X
    for i in range(len(S) - 2):
        #Convert the string to integer
        X = int(S[i : i + 3])

        #Find the difference between 753 and X
        diff = abs(X - 753)

        #If the difference is smaller than the current minimum difference, update the minimum difference
        if diff < min_diff:
            min_diff = diff

    #Print the minimum difference
    print(min_diff)

=======
Suggestion 9

def main():
    # 1. input
    s = input()

    # 2. process
    # 2.1. create a list of possible triplets
    # 2.2. calculate the absolute difference between each triplet and 753
    # 2.3. return the minimum of the differences
    # 3. output
    print(min([abs(int(s[i:i+3]) - 753) for i in range(len(s)-2)]))
