def main():
    v,a,b,c = map(int,input().split())
    if (v-a)%min(b,c) == 0:
        print("F")
    else:
        print("M")

if __name__ == '__main__':
    main()