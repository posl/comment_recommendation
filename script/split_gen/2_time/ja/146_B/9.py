def main():
    N = int(input())
    S = input()
    def change(S):
        return chr((ord(S) - ord('A') + N) % 26 + ord('A'))
    print("".join(map(change, S)))
