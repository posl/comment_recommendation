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
