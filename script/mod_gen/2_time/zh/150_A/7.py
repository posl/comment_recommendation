def main():
    # N,K = map(int,input().split(" "))
    # R,S,P = map(int,input().split(" "))
    # T = input()
    N,K = 5,2
    R,S,P = 8,7,6
    T = "rsrpr"
    # N,K = 7,1
    # R,S,P = 100,10,1
    # T = "ssssppr"
    # N,K = 30,5
    # R,S,P = 325,234,123
    # T = "rspsspspsrpspsppprpsprpspsppprpr"
    result = 0
    for i in range(N):
        if i < K:
            if T[i] == "r":
                result += P
            elif T[i] == "s":
                result += R
            else:
                result += S
        else:
            if T[i] == "r":
                if T[i-K] == "r":
                    if R <= P:
                        result += P
                    else:
                        result += R
                elif T[i-K] == "s":
                    result += P
                else:
                    result += R
            elif T[i] == "s":
                if T[i - K] == "r":
                    result += R
                elif T[i - K] == "s":
                    if S <= R:
                        result += R
                    else:
                        result += S
                else:
                    result += S
            else:
                if T[i - K] == "r":
                    result += P
                elif T[i - K] == "s":
                    result += S
                else:
                    if P <= S:
                        result += S
                    else:
                        result += P
    print(result)

if __name__ == '__main__':
    main()