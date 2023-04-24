Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    S_min = S
    S_max = S
    for i in range(len(S)):
        S_min = min(S_min, S[i:] + S[:i])
        S_max = max(S_max, S[i:] + S[:i])
    print(S_min)
    print(S_max)
    return

=======
Suggestion 2

def main():
    S = input()
    S = S + S
    S_min = S
    S_max = S
    for i in range(len(S)//2):
        if S[i:i+len(S)//2] < S_min:
            S_min = S[i:i+len(S)//2]
        if S[i:i+len(S)//2] > S_max:
            S_max = S[i:i+len(S)//2]
    print(S_min)
    print(S_max)

=======
Suggestion 3

def solution(S):
    # write your code in Python 3.6
    min_str = S
    max_str = S
    for i in range(1, len(S)):
        S = S[1:] + S[0]
        if S < min_str:
            min_str = S
        if S > max_str:
            max_str = S
    return min_str, max_str

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    s_list = [s]
    for i in range(1,n):
        s_list.append(s[i:] + s[:i])
    print(min(s_list))
    print(max(s_list))

=======
Suggestion 5

def main():
    s = input()
    s = s + s
    min = s
    max = s
    for i in range(len(s)):
        if s[i:i+len(s)//2] < min:
            min = s[i:i+len(s)//2]
        if s[i:i+len(s)//2] > max:
            max = s[i:i+len(s)//2]
    print(min)
    print(max)

=======
Suggestion 6

def lexicographical_order(S):
    #This function determines the lexicographical order between different strings S and T.
    #Simply speaking, the lexicographical order is the order in which words are listed in a dictionary.
    #As a more formal definition, here is the algorithm to determine the lexicographical order between different strings S and T.
    #Below, let S_i denote the i-th character of S. Also, if S is lexicographically smaller than T, we will denote that fact as S < T; if S is lexicographically larger than T, we will denote that fact as S > T.
    # Let L be the smaller of the lengths of S and T. For each i=1,2,...,L, we check whether S_i and T_i are the same. 
    # If there is an i such that S_i ≠ T_i, let j be the smallest such i. Then, we compare S_j and T_j. If S_j comes earlier than T_j in alphabetical order, we determine that S < T and quit; if S_j comes later than T_j, we determine that S > T and quit.
    #  
    # If there is no i such that S_i ≠ T_i, we compare the lengths of S and T. If S is shorter than T, we determine that S < T and quit; if S is longer than T, we determine that S > T and quit. 
    #
    #Input
    #S: a non-empty string consisting of lowercase English letters.
    #Output
    #A list with two elements: the lexicographically smallest and largest strings obtained by performing zero or more left shifts and zero or more right shifts on S.
    #Here, S_{min} and S_{max} are respectively the lexicographically smallest and largest strings obtained by performing zero or more left shifts and zero or more right shifts on S.
    #By performing shifts, we can obtain four strings: aaab, aaba, abaa, baaa. The lexicographically smallest and largest among them are aaab and baaa, respectively.
    #
    #Sample Input 1
    #aaba
    #
    #Sample Output 1
    #['aaab', 'baaa']
    #
    #Sample Input 2
    #z
    #
    #Sample Output 2
    #['z', 'z

=======
Suggestion 7

def left_shift(s):
    return s[1:] + s[0]

=======
Suggestion 8

def shiftLeft(s):
    return s[1:] + s[0]

=======
Suggestion 9

def shiftString(string):
    return string[1:] + string[0]
