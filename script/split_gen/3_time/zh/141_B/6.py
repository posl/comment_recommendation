def main():
    s=input()
    print("Yes" if all([s[i] in "RUD" for i in range(0,len(s),2)]) and all([s[i] in "LUD" for i in range(1,len(s),2)]) else "No")
