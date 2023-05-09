def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    # First, we will make a list of the time that each Snuke will receive a gem from Takahashi
    # We will call this list 'TakahashiTimes'. We will also make a list of the time that each Snuke
    # will receive a gem from another Snuke. We will call this list 'SnukeTimes'.
    TakahashiTimes = []
    SnukeTimes = []
    for i in range(N):
        TakahashiTimes.append(T[i])
        SnukeTimes.append(T[i] + S[i])
    # Now, we will go through the list of Snuke times and for each Snuke time, we will
    # determine the Snuke that will give the gem to the Snuke in question. We will call this
    # Snuke 'Receiver' and we will call the Snuke that gives the gem 'Giver'.
    # We will use a while loop to determine the time that the Receiver will receive the gem from
    # the Giver. The while loop will run until the Receiver receives a gem from Takahashi.
    # We will call the time that the Receiver receives the gem from the Giver 'GiverTime'.
    # We will call the time that the Receiver receives the gem from Takahashi 'TakahashiTime'.
    # We will call the time that the Receiver receives the gem from another Snuke 'SnukeTime'.
    # We will also call the index of the Receiver 'ReceiverIndex'.
    # We will call the index of the Giver 'GiverIndex'.
    # We will call the index of the Snuke that will give the gem to the Receiver after the Giver
    # 'NextGiverIndex'.
    # We will call the time that the Snuke that will give the gem to the Receiver after the Giver
    # will give the gem 'NextGiverTime'.
    # We will call the time that the Receiver receives the gem from the Snuke that will give the
    # gem to the Receiver after the Giver 'NextSnukeTime'.
    # We will call the time that the Receiver receives the gem from the Snuke that will give the
