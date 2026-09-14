# PLP Python Week 4

## Files

- `grade_reporter.py` - A program that assigns grades, counts passes and failures, and calculates the average score.
- `bug_hunt.py` - A debugging exercise that fixes three bugs and calculates the sum of numbers 1 to 5.


The hardest bug to find in Part B was the incorrect `while` condition because it did not produce an error message. I knew something was wrong because the program was supposed to add 1, 2, 3, 4, and 5, but the condition `count < 5` stopped before 5 was included, giving the wrong answer instead of 15.