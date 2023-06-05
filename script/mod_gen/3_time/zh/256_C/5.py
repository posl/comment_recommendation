def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    ans = 0
    for i in range(1,31):
        for j in range(1,31):
            for k in range(1,31):
                if i+j+k==h1 and i+j+k==h2 and i+j+k==h3 and i+j+k==w1 and i+j+k==w2 and i+j+k==w3:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()