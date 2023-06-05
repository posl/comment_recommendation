def main():
    x = int(input())
    for a in range(-118,119):
        for b in range(-119,118):
            if a**5 - b**5 == x:
                print(a,b)
                return
