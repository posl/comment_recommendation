def main():
    #input
    S = input()
    #compute
    S_set = set(S)
    #output
    if len(S_set) == 2:
        print("Yes")
    else:
        print("No")
