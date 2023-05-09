def main():
    #Read input
    N = int(input())
    S = input()
    #Check if S is a concatenation of two copies of some string
    if S == S[:N//2] * 2:
        print("Yes")
    else:
        print("No")
