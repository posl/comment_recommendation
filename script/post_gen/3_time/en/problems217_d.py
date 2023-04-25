Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            idx = cuts.index(x)
            print(cuts[idx+1] - cuts[idx-1])

=======
Suggestion 2

def main():
    l, q = map(int, input().split())
    cuts = [0, l]
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            i = cuts.index(x)
            print(cuts[i] - cuts[i - 1])

=======
Suggestion 3

def main():
    l, q = map(int, input().split())
    cuts = [0, l]
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            for i in range(len(cuts)):
                if cuts[i] == x:
                    print(cuts[i+1] - cuts[i-1])
                    break

=======
Suggestion 4

def main():
    l, q = map(int, input().split())
    cuts = [0, l]
    for i in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            idx = cuts.index(x)
            print(cuts[idx + 1] - cuts[idx - 1])

=======
Suggestion 5

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            for i in range(len(cut)):
                if cut[i] == x:
                    print(cut[i+1] - cut[i-1])
                    break

=======
Suggestion 6

def main():
    l, q = map(int, input().split())
    cut = [0, l]
    for i in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            idx = cut.index(x)
            print(cut[idx + 1] - cut[idx - 1])

=======
Suggestion 7

def main():
    l, q = map(int, input().split())
    cuts = [0,l]
    for _ in range(q):
        c,x = map(int, input().split())
        if c == 1:
            cuts.append(x)
            cuts.sort()
        else:
            left = cuts[bisect.bisect_left(cuts, x)-1]
            right = cuts[bisect.bisect_right(cuts, x)]
            print(right-left)
    return

=======
Suggestion 8

def main():
    L,Q = map(int,input().split())
    cut = [0,L]
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            index = cut.index(x)
            print(cut[index+1]-cut[index])
main()

=======
Suggestion 9

def main():
  L, Q = map(int, input().split())
  arr = [0, L]
  for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
      arr.append(x)
    else:
      arr.sort()
      index = arr.index(x)
      print(arr[index] - arr[index - 1])

=======
Suggestion 10

def get_input():
    input_line = input()
    input_line = input_line.split(" ")
    l = int(input_line[0])
    q = int(input_line[1])
    queries = []
    for i in range(q):
        input_line = input()
        input_line = input_line.split(" ")
        queries.append((int(input_line[0]), int(input_line[1])))
    return l, q, queries
