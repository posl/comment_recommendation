def main():
    #input
    N = int(input())
    S = [input() for _ in range(N)]
    #create a dictionary
    D = {}
    for s in S:
        if s[0] == '!':
            D[s[1:]] = 1
        else:
            D[s] = 0
    #output
    for s in S:
        if s[0] == '!':
            if D[s[1:]] == 0:
                print(s[1:])
                return
        else:
            if D[s] == 1:
                print(s)
                return
    print('satisfiable')
