def main():
    N = int(input())
    S = input()
    for i in range(len(S)):
        print(chr(ord("A")+(ord(S[i])-ord("A")+N)%26),end="")
    print()
