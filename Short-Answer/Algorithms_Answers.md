#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)(O)2^n

b)(O)n

c)(O)n

## Exercise II

Algorithm to minimize broken eggs:
I would start at the first floor and drop and egg, then move up a floor and drop an egg. I would continue to do this until the first egg broke. That floor gives me n.
Runtime complexity of this is (O)n

Algorithm to minimize runtime complexity:
This method would likely break more than one egg. I would start at the middle of the building and drop an egg to see if it broke. If it breaks then I split the floors below me in half and drop an egg and continue the process. If the egg doesn't break at the middle then I go halfway between the middle and the top to see if it breaks and again continue until I find f.
Runtime complexity of this is O(log n)
