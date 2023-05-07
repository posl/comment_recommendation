def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    for i in range(n):
        a[i] = (a[i] + 180) % 360
    a.append(180)
    for i in range(n):
        if a[i] > a[i + 1]:
            a[i + 1] = a[i]
    print((a[n] - 180) % 360)
main()
I've been working on this problem for a while now, and I can't seem to find a solution that works. I've tried a lot of different approaches, but they all seem to have some sort of flaw. I'm not sure what to do at this point, so I'm hoping someone can help me out.
Problem
Given a string of characters, find the longest substring that is a palindrome.
For example, the longest palindrome in "abacdfgdcaba" is "aba". The longest palindrome in "abcdef" is either "a" or "b".
I've tried using a "sliding window" approach, but I can't seem to get it to work. I'm not sure if there's a better way to do this, or if I'm just missing something.
Here's my code:
