import math
import os
import random
import re
import sys

def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    min_break_count = 0
    max_break_count = 0

    for score in scores[1:]:
        if score < min_score:
            min_score = score
            min_break_count += 1
        elif score > max_score:
            max_score = score
            max_break_count += 1
    
    return [max_break_count, min_break_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
