# https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/
# This is a program trying to solve the question from this reddit post ^

# Warmup 1 - remove 0s from a sequence:

def warm1(seq):
    for x in seq:
        if x == 0:
            seq.remove(x)


# Warmup 2 - sort list in descending order:


def warm2(seq):
    seq.sort(reverse=True)


# Warmup 3 = length check:

def warm3(seq, n):
    if n <= len(seq):
        return False
    else:
        return True


# Warmup 4 - front elimination:

def warm4(seq, n):
    loc = 0
    for x in seq[0:n]:
        seq[loc] = seq[loc] - 1
        loc = loc + 1
    return seq


# Challenge: the Havel-Hakimi algorithm


def hh(seq):
    while True:
        warm1(seq)
        if len(seq) <= 0:
            return True

        warm2(seq)
        n = seq.pop(0)
        if n > len(seq):
            return False

        warm4(seq, n)
        print(seq)


print(hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))
