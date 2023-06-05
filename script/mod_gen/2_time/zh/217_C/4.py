def main():
    S = []
    for i in range(3):
        S.append(input())
    
    if "ABC" not in S:
        print("ABC")
    elif "ARC" not in S:
        print("ARC")
    elif "AGC" not in S:
        print("AGC")
    elif "AHC" not in S:
        print("AHC")

if __name__ == '__main__':
    main()