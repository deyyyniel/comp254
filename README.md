# Lab Assignment #2 – Algorithm Analysis

Purpose: The purpose of this Lab assignment is to:

-   Perform experimental analysis of algorithms

-   Explain and proof the running time of algorithms in terms of big-Oh
    notation

-   Design various algorithm that achieve a specified running time

References: Read the course’s text chapter 4 and the lecture slides.
This material provides the necessary information that you need to
complete the exercises.


## Exercise 1

**If your first name starts with a letter from A-J inclusively:**

1.  Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example1** method from **Exercises.java** class in
    Lesson 4 examples.

2.  Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example2** method from **Exercises.java** class in
    Lesson 4 examples.

3.  Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example3** method from **Exercises.java** class in
    Lesson 4 examples.

4.  Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example4** method from **Exercises.java** class in
    Lesson 4 examples.

5.  Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example5** method from **Exercises.java** class in
    Lesson 4 examples.

For each of the above questions, use comments in the code to provide the
results and a brief explanation.

**If your first name starts with a letter from K-Z inclusively:**

1.  . Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example1** method from **Exercises2.java** class in
    Lesson 4 examples.

2.  Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example2** method from **Exercises2.java** class in
    Lesson 4 examples.

3.  Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example3** method from **Exercises.2java** class in
    Lesson 4 examples.

4.  Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example4** method from **Exercises2.java** class in
    Lesson 4 examples.

5.  Give a big-Oh characterization, in terms of **n**, of the running
    time of the **example5** method from **Exercises2.java** class in
    Lesson 4 examples.

(3 marks)

## Exercise 2

**If your first name starts with a letter from A-J inclusively:**

Perform an **experimental analysis** of the two algorithms
*prefixAverage1* and *prefixAverage2*, from lesson examples. Optionally,
visualize their running times as **a function of the input size** with a
**log-log chart**. Use either Java or Python graphical capabilities for
visualization.

**Hint**: Choose representative values of the input size **n**, similar
to *StringExperiment.java* from class examples.

**If your first name starts with a letter from K-Z inclusively:**

For each of the algorithms *unique1* and *unique2* (*Uniqueness.java*
class in Lesson 4 examples) which solve the element uniqueness problem,
perform an experimental analysis to determine the largest value of
***n*** such that the given algorithm runs in one minute or less.

**Hint**: Do a type of “binary search” to determine the maximum
effective value of ***n*** for each algorithm.

> (4 marks)

## Exercise 3

**If your first name starts with a letter from A-J inclusively:**

An array A contains n−1 unique integers in the range \[0,n−1\], that is,
there is one number from this range that is not in A. Design an
O(n)-time algorithm for finding that number. You are only allowed to use
O(1) additional space besides the array A itself. Write the java method
that implements this algorithm and a main method to test it.

**Hint:** Numbers in \[0, n-1\] form an arithmetic progression whose sum
is known.

**If your first name starts with a letter from K-Z inclusively:**

Given an array A of n arbitrary integers, design an O(n)-time algorithm
for finding an integer that cannot be formed as the sum of two integers
in A. Write the java method that implements this algorithm and a main
method to test it.

**Hint** The sum of every two integers in A is always less or equal to
twice the maximum element.

> (3 marks)

**Evaluation:**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Functionality</strong></p>
<ul>
<li><p>Correct result of running time</p></li>
<li><p>Correct experimental analyses code and visualization</p></li>
<li><p>Code demonstration and brief explanation of proof or analyses in
a short video</p></li>
</ul></th>
<th><p>20%</p>
<p>40%</p>
<p>10%</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Object Oriented Design</strong></p>
<ul>
<li><p>Correct design of classes and methods similarly to chapter 3
examples.</p></li>
<li><p>Correct use of generics</p></li>
<li><p>Correct use of naming guidelines for classes, variables, methods,
packages.</p></li>
</ul></td>
<td><p>15%</p>
<p>5%</p></td>
</tr>
<tr class="even">
<td><strong>Friendly graphical display</strong></td>
<td>10%</td>
</tr>
<tr class="odd">
<td><strong>Total</strong></td>
<td>100%</td>
</tr>
</tbody>
</table>

**Naming and Submission Rules:**

You must **name your Eclipse project** according to the following rule:

**YourFullname_COMP254Labnumber**. Example: **JohnSmith_COMP254Lab2**

You must name package names
**com.exercisenumber.yourfirstname.yourlastname**, for example:
**com.exercise1.john.smith**

Provide your **student number and full name as a comment** at the top of
main method for each exercise.

**Archive your project in a zip file** named according to the following
rule:

**YourFullname_COMP254Labnumber.zip**

Example: **JohnSmith_COMP254Lab2.zip**

Upload the zip file on eCentennial using the Assignment link.