Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    L = int(input())
    ans = 0
    for a in range(1, L):
        for b in range(1, L):
            if a + b >= L:
                break
            c = L - a - b
            ans = max(ans, a * b * c)
    print(ans)

=======
Suggestion 2

def main():
    L = int(input())
    ans = (L/3)**3
    print(ans)

=======
Suggestion 3

def main():
    L = int(input())
    print((L/3)**3)

=======
Suggestion 4

def get_max_volume(L):
    max_volume = 0
    for i in range(1, L):
        for j in range(1, L):
            k = L - i - j
            if k < 1:
                break
            max_volume = max(max_volume, i * j * k)
    return max_volume

L = int(input())
print(get_max_volume(L))

=======
Suggestion 5

def main():
    L = int(input())
    print(((L/3)**3))
