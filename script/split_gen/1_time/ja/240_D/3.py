def main():
    N = int(input())
    A = list(map(int, input().split()))
    balls = [0] * (2*10**5+1)
    for a in A:
        balls[a] += 1
        print(sum(balls))
