#Problem Statement
#We have a playlist with N songs numbered 1,…,N.
#Song i lasts A_i seconds.
#When the playlist is played, song 1, song 2, …, and song N play in this order. When song N ends, the playlist repeats itself, starting from song 1 again. 
#While a song is playing, the next song does not play; when a song ends, the next song starts immediately.
#At exactly T seconds after the playlist starts playing, which song is playing? Also, how many seconds have passed since the start of that song?
#There is no input where the playlist changes songs at exactly T seconds after it starts playing.
#
#Constraints
#1≤N≤10^5
#1≤T≤10^18
#1≤A_i≤10^9
#The playlist does not change songs at exactly T seconds after it starts playing.
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N T
#A_1 … A_N
#
#Output
#Print an integer representing the song that is playing at exactly 
#T seconds after the playlist starts playing, and an integer representing the number of seconds that have passed since the start of that song, separated by a space.
#
#Sample Input 1
#3 600
#180 240 120
#
#Sample Output 1
#1 60
#
#Sample Input 2
#3 281
#94 94 94
#
#Sample Output 2
#3 93
#
#Sample Input 3
#10 5678912340
#1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
#
#Sample Output 3
#6 678912340

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t %= sum(a)
    for i in range(n):
        if t < a[i]:
            print(i + 1, t)
            break
        t -= a[i]

if __name__ == '__main__':
    main()