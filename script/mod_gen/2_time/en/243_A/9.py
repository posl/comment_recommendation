def main():
    #Read the input
    v,a,b,c = map(int,input().split())
    #The first person to run short of shampoo is Takahashi's father
    if a > v:
        print("F")
    #The first person to run short of shampoo is Takahashi's mother
    elif a + b > v:
        print("M")
    #The first person to run short of shampoo is Takahashi
    else:
        print("T")

if __name__ == '__main__':
    main()