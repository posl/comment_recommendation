def problem146_b():
    N = int(input())
    S = input()
    for i in range(len(S)):
        tmp = ord(S[i]) + N
        if tmp > ord('Z'):
            tmp = tmp - ord('Z') + ord('A') - 1
        print(chr(tmp),end='')

if __name__ == '__main__':
    problem146_b()