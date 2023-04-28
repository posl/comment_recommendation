Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    print(L, R)
    return

=======
Suggestion 2

def solve():
    n = int(input())
    intervals = []
    for _ in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r))
    intervals.sort(key=lambda x: x[0])
    ans = []
    l, r = intervals[0]
    for i in range(1, n):
        nl, nr = intervals[i]
        if r < nl:
            ans.append((l, r))
            l, r = nl, nr
        else:
            r = max(r, nr)
    ans.append((l, r))
    for l, r in ans:
        print(l, r)

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    for i in range(n):
        l,r = map(int,input().split())
        a.append([l,r])
    a.sort()
    l = a[0][0]
    r = a[0][1]
    for i in range(1,n):
        if a[i][0] <= r:
            r = max(r,a[i][1])
        else:
            print(l,r)
            l = a[i][0]
            r = a[i][1]
    print(l,r)
main()

=======
Suggestion 4

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(tuple(map(int, input().split())))
    l.sort()
    a = l[0][0]
    b = l[0][1]
    for i in range(1, n):
        if l[i][0] <= b:
            if l[i][1] > b:
                b = l[i][1]
        else:
            print(a, b)
            a = l[i][0]
            b = l[i][1]
    print(a, b)

=======
Suggestion 5

def main():
    n = int(input())
    intervals = []
    for i in range(n):
        intervals.append(list(map(int, input().split())))
    intervals.sort(key=lambda x: x[0])
    result = []
    result.append(intervals[0])
    for i in range(1, n):
        if intervals[i][0] < result[-1][1]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])
    for i in range(len(result)):
        print(result[i][0], result[i][1])

=======
Suggestion 6

def solve():
    N = int(input())
    L = []
    for _ in range(N):
        l, r = map(int, input().split())
        L.append((l, r))
    L.sort()
    ans = []
    l, r = L[0]
    for i in range(1, N):
        if r >= L[i][0]:
            r = max(r, L[i][1])
        else:
            ans.append((l, r))
            l, r = L[i]
    ans.append((l, r))
    for l, r in ans:
        print(l, r)

=======
Suggestion 7

def main():
    N = int(input())
    LR = []
    for _ in range(N):
        LR.append(list(map(int, input().split())))

    LR.sort(key=lambda x: x[0])

    left = LR[0][0]
    right = LR[0][1]

    for i in range(1, N):
        if LR[i][0] <= right:
            right = max(right, LR[i][1])
        else:
            print(left, right)
            left = LR[i][0]
            right = LR[i][1]

    print(left, right)

=======
Suggestion 8

def main():
    n = int(input())
    intervals = []
    for i in range(n):
        intervals.append([int(x) for x in input().split()])

    intervals.sort(key=lambda x: x[0])

    end = intervals[0][1]
    start = intervals[0][0]

    for i in range(1, n):
        if intervals[i][0] > end:
            print(start, end)
            start = intervals[i][0]
            end = intervals[i][1]
        else:
            end = max(end, intervals[i][1])

    print(start, end)

=======
Suggestion 9

def main():
    n = int(input())
    lines = []
    for _ in range(n):
        lines.append(list(map(int, input().split())))
    lines.sort(key=lambda x: x[0])
    result = []
    cur = lines[0]
    for i in range(1, n):
        if lines[i][0] <= cur[1]:
            cur[1] = max(cur[1], lines[i][1])
        else:
            result.append(cur)
            cur = lines[i]
    result.append(cur)
    for line in result:
        print(line[0], line[1])

=======
Suggestion 10

def main():
    # Get the number of intervals.
    n = int(input())

    # Create a list of intervals.
    intervals = []
    for i in range(n):
        # Get the interval.
        interval = input().split(' ')
        # Append the interval to the list of intervals.
        intervals.append((int(interval[0]), int(interval[1])))

    # Sort the intervals by their left end.
    intervals.sort(key=lambda tup: tup[0])

    # Initialize the list of merged intervals.
    merged_intervals = []
    # Initialize the first interval.
    merged_intervals.append(intervals[0])

    # Iterate through the intervals.
    for i in range(1, n):
        # Get the current interval.
        current_interval = intervals[i]
        # Get the last interval in the list of merged intervals.
        last_interval = merged_intervals[-1]

        # Check if the current interval and the last interval overlap.
        if current_interval[0] >= last_interval[0] and current_interval[0] < last_interval[1]:
            # Check if the current interval is longer than the last interval.
            if current_interval[1] > last_interval[1]:
                # Update the last interval.
                merged_intervals[-1] = (last_interval[0], current_interval[1])
        else:
            # Append the current interval to the list of merged intervals.
            merged_intervals.append(current_interval)

    # Iterate through the merged intervals.
    for i in range(len(merged_intervals)):
        # Get the merged interval.
        merged_interval = merged_intervals[i]
        # Print the merged interval.
        print(merged_interval[0], merged_interval[1])
