def main():
    N = int(input())
    S = input()
    #print(N,S)
    R = 0
    G = 0
    B = 0
    for i in range(N):
        if S[i] == "R":
            R += 1
        elif S[i] == "G":
            G += 1
        elif S[i] == "B":
            B += 1
    #print(R,G,B)
    ans = R * G * B
    #print(ans)
    for i in range(N):
        for j in range(i+1,N):
            k = 2*j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()