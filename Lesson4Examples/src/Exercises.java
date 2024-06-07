class Exercises {

  public static int example1(int[] arr) {
    int n = arr.length, total = 0; // O(1) - Getting the length of arr and initializing total
    for (int j = 0; j < n; j++) // O(n) - Loop runs n times
      total += arr[j]; // O(1) - Accessing an element and addition are constant time operations
    return total; // O(1) - Returning the total
    // Overall Time Complexity: O(n)
  }

  public static int example2(int[] arr) {
    int n = arr.length, total = 0; // O(1) - Getting the length of arr and initializing total
    for (int j = 0; j < n; j += 2) // O(n/2) - Loop runs n/2 times (still O(n) in big-Oh notation)
      total += arr[j]; // O(1) - Accessing an element and addition are constant time operations
    return total; // O(1) - Returning the total
    // Overall Time Complexity: O(n)
  }

  public static int example3(int[] arr) {
    int n = arr.length, total = 0; // O(1) - Getting the length of arr and initializing total
    for (int j = 0; j < n; j++) // O(n) - Outer loop runs n times
      for (int k = 0; k <= j; k++) // O(j+1) - Inner loop runs (j+1) times
        total += arr[j]; // O(1) - Accessing an element and addition are constant time operations
    // Total time complexity for the nested loops is the sum of the series 1 + 2 + 3
    // + ... + n, which is O(n^2)
    return total; // O(1) - Returning the total
    // Overall Time Complexity: O(n^2)
  }

  public static int example4(int[] arr) {
    int n = arr.length, prefix = 0, total = 0; // O(1) - Getting the length of arr and initializing variables
    for (int j = 0; j < n; j++) { // O(n) - Loop runs n times
      prefix += arr[j]; // O(1) - Accessing an element and addition are constant time operations
      total += prefix; // O(1) - Addition is a constant time operation
    }
    return total; // O(1) - Returning the total
    // Overall Time Complexity: O(n)
  }

  public static int example5(int[] first, int[] second) {
    int n = first.length, count = 0; // O(1) - Getting the length of first and initializing count
    for (int i = 0; i < n; i++) { // O(n) - Outer loop runs n times
      int total = 0; // O(1) - Initializing total
      for (int j = 0; j < n; j++) // O(n) - Middle loop runs n times
        for (int k = 0; k <= j; k++) // O(j+1) - Inner loop runs (j+1) times
          total += first[k]; // O(1) - Accessing an element and addition are constant time operations
      // Total time complexity for the nested loops is O(n^2) for the j-loop and
      // k-loop
      if (second[i] == total)
        count++; // O(1) - Comparison and increment are constant time operations
    }
    // The overall time complexity is O(n) * O(n^2) = O(n^3)
    return count; // O(1) - Returning the count
    // Overall Time Complexity: O(n^3)
  }
}
