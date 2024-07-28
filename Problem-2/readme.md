
# Subarray Division HackerRank Problem

wo children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birthday.
Determine how many ways she can divide the chocolate.

## Example

```javascript
s = [2,2,1,3,2]
d = 4
m = 2
```
Lily wants to find segments summing to Ron's birthday, d=4  with a length equalling his birth month, m=4. In this case, there are two segments meeting her criteria: [2,2] and [1,3].

<p><strong>Function Description</strong></p>

complete the birthday function in the editor below

<ul>
  birthday has the following parameter(s):
</ul>
<li>int s[n]: the numbers on each of the squares of chocolate</li>
<li>int d: Ron's birth day</li>
<li>int m: Ron's birth month</li>

<p><strong>Returns</strong></p>

int: the number of ways the bar can be divided

