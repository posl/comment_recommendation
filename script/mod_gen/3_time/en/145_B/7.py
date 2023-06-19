def main():
    N = int(input())
    S = input()
    if S == S[0:int(N/2)] * 2:
        print("Yes")
    else:
        print("No")
main()
