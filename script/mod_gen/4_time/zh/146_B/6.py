def problem146_b():
    N = int(input())
    S = input()
    result = ""
    for i in range(len(S)):
        if ord(S[i]) + N > 90:
            result += chr(ord(S[i]) + N - 26)
        else:
            result += chr(ord(S[i]) + N)
    print(result)

if __name__ == '__main__':
    problem146_b()