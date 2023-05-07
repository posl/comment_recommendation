def main():
    R = int(input())
    if 0 <= R <= 1199:
        print("ABC")
    elif 1200 <= R <= 2799:
        print("ARC")
    elif 2800 <= R <= 4208:
        print("AGC")

if __name__ == '__main__':
    main()