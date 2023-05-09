def main():
    # Take input here
    S = input()
    T = input()
    # Computing result
    result = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            result += 1
    # Print result
    print(result)
