"""
write payouts based off
https://wizardofodds.com/games/video-poker/strategy/jacks-or-better/9-6/optimal/
"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))


combination(10, 5)


hands = {
    "royal_flush": 800,
    "straight_flush": 50,
    "four_of_a_kind": 25,
    "full_house": 9,
    "flush": 6,
    "straight": 4,
    "three_of_a_kind": 3,
    "two_pair": 2,
    "jacks_or_better": 1,
    "loss": 0
}
