def main():
    abc = input()
    bca = abc[1] + abc[2] + abc[0]
    cab = bca[1] + bca[2] + bca[0]
    print(int(abc) + int(bca) + int(cab))
