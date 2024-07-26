<h1> DSA Problem-1 </h1>
<p> Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.</p>

<p><strong> Example </strong></p>
<p> scores = [ 12,24,10,24 ] </p>
<p> Scores are in the same order as the games played. She tabulates her results as follows: </p>
<pre>
    Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1
</pre>
<p> Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season. </p>
<p> <strong><b> Function Description: </b></strong></p>
<p>Complete the breakingRecords function in the editor below. breakingRecords has the following parameter(s):
<ul>
  <li> int scores[n]: points scored per game</li>
</ul>
</p>
<p><strong><b>Returns:</b></strong></p>
<ul>
  <li> int[2]: An array with the number of times she broke her records. Index 0 is for breaking most points records, and index 1 is for breaking the least points records.</li>
</ul>
<p><b>Input Format:</b></p>
<p> The first line contains an integer n, the number of games.
The second line contains  space-separated integers describing the respective values of score0,score1...., score n-1.</p>

<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
  <li><code>0 &lt;= score[i] &lt;= 10<sup>8</sup></code></li>
</ul>
<p><strong class="example">Sample Input 0:</strong></p>
<pre>
9
10 5 20 20 4 5 2 25 1
</pre>
<p><strong class="example">Sample Output 0:</strong></p>
<pre>
2 4 
</pre>
<p> <strong> Explanation 0 </strong></p>
<p> The diagram below depicts the number of times Maria broke her best and worst records throughout the season: </p>
![image alt](https://github.com/sameer6699/Hacker-Rank-DSA-1/blob/4435f1543dd8125a7257639b8bb71cad5863973c/1.jpg)
