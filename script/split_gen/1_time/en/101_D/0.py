def main():
    k = int(input())
    snuke = [1]
    for i in range(k):
        print(snuke[i])
        snuke.append(snuke[i]*10)
        snuke.append(snuke[i]*10+1)
main()
This code is a bit slow, but it works. I tried to solve this problem in a more efficient way, but I couldn’t. I’ll try to solve it later.
I got 100 points for this problem.
