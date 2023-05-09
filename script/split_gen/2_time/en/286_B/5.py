def main():
    N = int(input())
    S = input()
    # Replace all contiguous occurrences of na in S with nya.
    S = S.replace("na", "nya")
    print(S)
main()
