def main():
    N = int(input())
    S = input()
    # N = 5
    # S = "LRRLR"
    # N = 7
    # S = "LLLLLLL"
    A = [0]
    for i in range(1,N+1):
        if S[i-1] == "L":
            A.insert(0,i)
        else:
            A.append(i)
    print(" ".join(map(str,A)))
