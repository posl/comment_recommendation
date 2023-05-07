def main():
    n = int(input())
    s = input()
    #print(n)
    #print(s)
    for i in range(n):
        if s[i] == "1":
            if i % 2 == 0:
                print("Takahashi")
            else:
                print("Aoki")
            break
