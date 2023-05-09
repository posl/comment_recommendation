def main():
    V, A, B, C = map(int, input().split())
    if V % A == 0:
        Takahashi = V // A
    else:
        Takahashi = V // A + 1
    if V % B == 0:
        Takahashi_father = V // B
    else:
        Takahashi_father = V // B + 1
    if V % C == 0:
        Takahashi_mother = V // C
    else:
        Takahashi_mother = V // C + 1
    if Takahashi_father <= Takahashi_mother and Takahashi_father <= Takahashi:
        print("F")
    elif Takahashi_mother <= Takahashi_father and Takahashi_mother <= Takahashi:
        print("M")
    elif Takahashi <= Takahashi_father and Takahashi <= Takahashi_mother:
        print("T")

if __name__ == '__main__':
    main()