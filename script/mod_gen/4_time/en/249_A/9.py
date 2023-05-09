def main():
    # Read input
    A, B, C, D, E, F, X = map(int, input().split())
    # Calculate the distance of Takahashi and Aoki
    distance_takahashi = (A + C) * B
    distance_aoki = D * E
    # Compare the distance of Takahashi and Aoki
    if distance_takahashi > distance_aoki:
        print("Takahashi")
    elif distance_aoki > distance_takahashi:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()