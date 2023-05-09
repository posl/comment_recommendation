def main():
    N = int(input())
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))
    #S and T are lists of integers
    #S[i] is the time it takes Snuke i to hand a gem to Snuke i+1
    #T[i] is the time that Takahashi will hand a gem to Snuke i
    #N is the number of Snuke's
    #S and T
