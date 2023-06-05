def main():
    # S = "RUDLUDR"
    # S = "DULL"
    # S = "uuuuuuuuuuuuu"
    # S = "ULURU"
    # S = "rdululdururlrdulrlr"
    S = input()
    result = "Yes"
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == "L":
                result = "No"
                break
        else:
            if S[i] == "R":
                result = "No"
                break
    print(result)
