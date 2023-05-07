def main():
    # Read the input data
    A, B, C, D = map(int, input().split())
    # Calculate the number of attacks necessary to bring the health to 0 or less
    takahashi_attacks = (A + D - 1) // D
    aoki_attacks = (C + B - 1) // B
    # If Takahashi's monster attacks first, Takahashi wins
    if takahashi_attacks <= aoki_attacks:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()