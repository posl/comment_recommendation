def main():
    # S = input()
    S = "rdululdururlrdulrlr"
    S_odd = S[::2]
    S_even = S[1::2]
    # print(S_odd)
    # print(S_even)
    if S_odd.count("R") == 0 and S_odd.count("L") == 0 and S_even.count("U") == 0 and S_even.count("D") == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()