def main():
    N = int(input())
    S = input()
    if S[0:int(N/2)] == S[int(N/2):]:
        print("Yes")
    else:
        print("No")
