public class Exercises2 {

	public static int example1(int n) {
		int sum = 0; // O(1) - Initializing sum
		for (int i = 1; i <= n; i++) // O(n) - Loop runs n times
			sum += i; // O(1) - Addition is a constant time operation
		return sum; // O(1) - Returning the sum
		// Overall Time Complexity: O(n)
	}

	public static int example2(int n) {
		int p = 1; // O(1) - Initializing p
		for (int i = 1; i <= 2 * n; i++) // O(2n) - Loop runs 2n times (still O(n) in big-Oh notation)
			p *= i; // O(1) - Multiplication is a constant time operation
		return p; // O(1) - Returning the product
		// Overall Time Complexity: O(n)
	}

	public static int example3(int n) {
		int p = 1; // O(1) - Initializing p
		for (int i = 1; i <= Math.pow(n, 2); i++) // O(n^2) - Loop runs n^2 times
			p *= i; // O(1) - Multiplication is a constant time operation
		return p; // O(1) - Returning the product
		// Overall Time Complexity: O(n^2)
	}

	public static int example4(int n) {
		int sum = 0; // O(1) - Initializing sum
		for (int i = 1; i <= 2 * n; i++) { // O(2n) - Outer loop runs 2n times (still O(n) in big-Oh notation)
			for (int j = 1; j <= i; j++) // O(i) - Inner loop runs i times
				sum += i; // O(1) - Addition is a constant time operation
		}
		// Total time complexity for the nested loops is the sum of the series 1 + 2 + 3
		// + ... + 2n, which is O(n^2)
		return sum; // O(1) - Returning the sum
		// Overall Time Complexity: O(n^2)
	}

	public static int example5(int n) {
		int sum = 0; // O(1) - Initializing sum
		for (int i = 1; i <= Math.pow(n, 2); i++) { // O(n^2) - Outer loop runs n^2 times
			for (int j = 1; j <= i; j++) // O(i) - Inner loop runs i times
				sum += i; // O(1) - Addition is a constant time operation
		}
		// Total time complexity for the nested loops is the sum of the series 1 + 2 + 3
		// + ... + n^2, which is O(n^4)
		return sum; // O(1) - Returning the sum
		// Overall Time Complexity: O(n^4)
	}
}
