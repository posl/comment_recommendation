def main():
    S = input()
    N = len(S)
    #count red
    red = 0
    for i in range(N):
        if S[i] == '0':
            red += 1
    #count blue
    blue = 0
    for i in range(N):
        if S[i] == '1':
            blue += 1
    #print the result
    print(min(red, blue) * 2)
