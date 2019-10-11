'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # setup counter
    counter = 0
    n = 0
    # Then recursively feed n+1 into the function until n = len(word)-1

    def check_for_th(n, word):
        nonlocal counter
        # Base cases
        if n == len(word)-1:
            return
        elif len(word) <= 1:
            return
        # See if n[0] and n[0+1] is "th", if so, add to results array
        elif word[n] + word[n+1] == 'th':
            counter += 1
        return check_for_th(n+1, word)
    check_for_th(n, word)
    return counter
