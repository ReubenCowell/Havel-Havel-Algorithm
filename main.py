# https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/
# This is a program trying to solve the question from this reddit post ^

# Warmup 1 - remove 0s from a sequence:
list = [5, 3, 0, 2, 6, 2, 0, 7, 2, 5]


def warm1(seq):
    for x in seq:
        if x == 0:
            seq.remove(x)


warm1(list)
print(list)
