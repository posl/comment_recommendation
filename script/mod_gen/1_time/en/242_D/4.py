def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        k -= 1
        while t > 0:
            if k < len(S) // 3:
                if S[k] == 'A':
                    S = 'BC' + S[3*k + 1:]
                elif S[k] == 'B':
                    S = 'CA' + S[3*k + 1:]
                elif S[k] == 'C':
                    S = 'AB' + S[3*k + 1:]
            elif k < 2 * len(S) // 3:
                if S[k] == 'A':
                    S = S[:k] + 'BC' + S[3*k - len(S) + 1:]
                elif S[k] == 'B':
                    S = S[:k] + 'CA' + S[3*k - len(S) + 1:]
                elif S[k] == 'C':
                    S = S[:k] + 'AB' + S[3*k - len(S) + 1:]
            else:
                if S[k] == 'A':
                    S = S[:k] + 'BC'
                elif S[k] == 'B':
                    S = S[:k] + 'CA'
                elif S[k] == 'C':
                    S = S[:k] + 'AB'
            k %= len(S)
            t -= 1
        print(S[k])
main()
I tried to solve this problem by using a Python script. I got a TLE error. How can I improve the speed of my code?
I think that the main problem is the following part:
S = S[:k] + 'BC' + S[3*k - len(S) + 1:]
I have to create a new string every time I modify S. This is very slow. But I don't know how to solve this problem. Is there any way to improve the speed of my code?

if __name__ == '__main__':
    main()