public class Exercises2 {

	public static int example1(int n) {
		int sum = 0;
		for (int i = 1; i <= n; i++)
			sum += i;
		return sum;
	}

	public static int example2(int n) {
		int p = 1;
		for (int i = 1; i <= 2 * n; i++)
			p *= i;
		return p;
	}

	public static int example3(int n) {
		int p = 1;
		for (int i = 1; i <= Math.pow(n, 2); i++)
			p *= i;
		return p;
	}

	public static int example4(int n) {
		int sum = 0;
		for (int i = 1; i <= 2 * n; i++) {
			for (int j = 1; j <= i; j++)
				sum += i;
		}
		return sum;
	}

	public static int example5(int n) {
		int sum = 0;
		for (int i = 1; i <= Math.pow(n, 2); i++) {
			for (int j = 1; j <= i; j++)
				sum += i;
		}
		return sum;
	}
}
