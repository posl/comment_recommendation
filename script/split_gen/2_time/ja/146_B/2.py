def main():
    N = int(input())
    S = input()
    ans = ""
    for c in S:
        ans += chr((ord(c)-ord('A')+N)%26+ord('A'))
    print(ans)
