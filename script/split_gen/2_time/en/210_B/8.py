def main():
    N = int(input())
    S = input()
    #print("N", N)
    #print("S", S)
    #print("S[0]", S[0])
    #print("S[1]", S[1])
    #print("S[1] == '1'", S[1] == '1')
    for i in range(N):
        if S[i] == '1':
            if i % 2 == 0:
                print("Takahashi")
            else:
                print("Aoki")
            break
