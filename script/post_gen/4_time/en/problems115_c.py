Synthesizing 10/10 solutions

=======
Suggestion 1

def   main (): 
     n ,   k   =   map ( int ,   input (). split ()) 
     h   =   [ int ( input ())   for   _   in   range ( n )] 
     h . sort () 
     ans   =   10 ** 9 
     for   i   in   range ( n   -   k   +   1 ): 
         ans   =   min ( ans ,   h [ i   +   k   -   1 ]   -   h [ i ]) 
     print ( ans )

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    print(min(h[i + K - 1] - h[i] for i in range(N - K + 1)))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    H.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, H[i+K-1] - H[i])
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1] - h[i])
    print(ans)

=======
Suggestion 5

def   main (): 
     N ,   K   =   map ( int ,   input (). split ()) 
     h   =   sorted ([ int ( input ())   for   _   in   range ( N )]) 
     ans   =   float ( 'inf' ) 
     for   i   in   range ( N   -   K   +   1 ): 
         ans   =   min ( ans ,   h [ i   +   K   -   1 ]   -   h [ i ]) 
     print ( ans )

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, h[i + K - 1] - h[i])
    print(ans)

main()

import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		int[] h = new int[N];
		for (int i = 0; i < N; i++) {
			h[i] = sc.nextInt();
		}
		Arrays.sort(h);
		int ans = Integer.MAX_VALUE;
		for (int i = 0; i < N - K + 1; i++) {
			ans = Math.min(ans, h[i + K - 1] - h[i]);
		}
		System.out.println(ans);
	}
}

import java.util.*;
import java.io.*;
import java.math.*;
public class Main {
	private static Scanner sc;
	private static Printer pr;
	static void solve() {
		int N = sc.nextInt();
		int K = sc.nextInt();
		int[] h = new int[N];
		for (int i = 0; i < N; i++) {
			h[i] = sc.nextInt();
		}
		Arrays.sort(h);
		int ans = Integer.MAX_VALUE;
		for (int i = 0; i < N - K + 1; i++) {
			ans = Math.min(ans, h[i + K - 1] - h[i]);
		}
		pr.println(ans);
	}
	// ---------------------------------------------------
	public static void main(String[] args) {
		sc = new Scanner(System.in);
		pr = new Printer(System.out);
			
		solve();
			
		pr.close();
		sc.close();
	}
	static class Scanner {
		BufferedReader br;
		StringTokenizer tok;
		Scanner (InputStream is) {
			br = new BufferedReader(new InputStreamReader(is));
		}
		void close () {
			try {
				br.close();
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
		}
		boolean hasNext() {
			while (tok == null || !tok.hasMoreTokens()) {
				String s = nextLine();
				if

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    H = sorted([int(input()) for _ in range(N)])
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, H[i + K - 1] - H[i])
    print(ans)

=======
Suggestion 8

def solve(n, k, h):
    h.sort()
    min_diff = h[-1] - h[0]
    for i in range(n - k + 1):
        min_diff = min(min_diff, h[i + k - 1] - h[i])
    return min_diff

=======
Suggestion 9

def main():
    from sys import stdin
    from bisect import bisect_left
    input = stdin.readline
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    H.sort()
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, H[i + K - 1] - H[i])
    print(ans)

=======
Suggestion 10

def main():
    #Get the number of trees and the number of trees to decorate
    N,K = map(int,input().split())

    #Get the height of each tree
    H = [int(input()) for i in range(N)]

    #Sort the heights
    H.sort()

    #Set the minimum difference to a large number
    min_diff = 10**10

    #Loop through the heights
    for i in range(N-K+1):
        #Calculate the difference between the first and last trees to decorate
        diff = H[i+K-1] - H[i]

        #If the difference is less than the current minimum difference
        if diff < min_diff:
            #Update the minimum difference
            min_diff = diff

    #Output the minimum difference
    print(min_diff)
