from random import shuffle

suits = ["H", "D", "S", "C"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


def load_deck(deck):
    for suit in suits:
        for rank in ranks:
            deck.append({
                "suit": suit,
                "rank": rank
            })
    return deck


def break_down(deck):
    card_map = {}
    suit_map = {}

    for card in deck:
        if card["rank"] not in card_map:
            card_map[card["rank"]] = 1
        else:
            card_map[card["rank"]] += 1

    for card in deck:
        if card["suit"] not in suit_map:
            suit_map[card["suit"]] = 1
        else:
            suit_map[card["suit"]] += 1

    return card_map, suit_map


def flush(deck):
    _, suit_map = break_down(deck)

    return len(suit_map) == 1


def single_pair(deck):

    map, _ = break_down(deck)
    one_count = 0
    two_count = 0

    for key, value in map.items():
        if value == 1:
            one_count += 1
        if value == 2:
            two_count += 1

    high_index = 0
    for key, value in map.items():
        if value == 2:
            index = ranks.index(key)
            high_index = index if index > high_index else high_index

    return one_count == 3 and two_count == 1 and high_index > 8


def two_pair(deck):
    map, _ = break_down(deck)

    one_count = 0
    two_count = 0

    for key, value in map.items():
        if value == 1:
            one_count += 1
        if value == 2:
            two_count += 1

    return one_count == 1 and two_count == 2


def full_house(deck):
    map, _ = break_down(deck)

    two_count = 0
    three_count = 0

    for key, value in map.items():
        if value == 2:
            two_count += 1
        if value == 3:
            three_count += 1

    return two_count == 1 and three_count == 1


def trips(deck):

    map, _ = break_down(deck)

    one_count = 0
    three_count = 0

    for key, value in map.items():
        if value == 1:
            one_count += 1
        if value == 3:
            three_count += 1

    return one_count == 2 and three_count == 1


def quads(deck):
    map, _ = break_down(deck)

    one_count = 0
    four_count = 0

    for key, value in map.items():
        if value == 1:
            one_count += 1
        if value == 4:
            four_count += 1

    return one_count == 1 and four_count == 1


def straight(deck):

    indexes = [ranks.index(c["rank"]) for c in deck]
    indexes.sort()

    if indexes == [0, 1, 2, 3, 12]:
        return True

    else:
        for i in range(4):
            if indexes[i] + 1 != indexes[i + 1]:
                return False

    return True


def straight_flush(deck):
    return straight(deck) and flush(deck)


def royal_flush(deck):
    indexes = [ranks.index(c["rank"]) for c in deck].sort()

    return straight_flush(deck) and indexes == [8, 9, 10, 11, 12]


def main():
    num_hands = input("How many hands do you want to draw? ")
    deck = []
    load_deck(deck)

    hands = {
        "royal_flush": 0,
        "straight_flush": 0,
        "four_of_a_kind": 0,
        "full_house": 0,
        "flush": 0,
        "straight": 0,
        "three_of_a_kind": 0,
        "two_pair": 0,
        "jacks_or_better": 0,
        "losses": 0
    }

    for _ in range(int(num_hands)):
        shuffle(deck)

        hand = deck[:5]

        if royal_flush(hand):
            hands["royal_flush"] += 1
        elif straight_flush(hand):
            hands["straight_flush"] += 1
        elif quads(hand):
            hands["four_of_a_kind"] += 1
        elif full_house(hand):
            hands["full_house"] += 1
        elif flush(hand):
            hands["flush"] += 1
        elif straight(hand):
            hands["straight"] += 1
        elif trips(hand):
            hands["three_of_a_kind"] += 1
        elif two_pair(hand):
            hands["two_pair"] += 1
        elif single_pair(hand):
            hands["jacks_or_better"] += 1
        else:
            hands["losses"] += 1

    print(hands)


if __name__ == "__main__":
    main()
