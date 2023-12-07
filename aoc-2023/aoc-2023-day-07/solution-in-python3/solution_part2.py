from functools import cmp_to_key
from collections import defaultdict

from helpers import fileutils

def get_char_freq_map_from_string(input):
    freq = {}
    for c in set(input):
       freq[c] = input.count(c)
    return freq

def check_char_freq(hand):
    freq = get_char_freq_map_from_string(hand)
    return sorted(freq.values(), reverse=True)

def get_max_same_card(hand):
    max_same = 0
    for i in range(len(hand)):
        same = 0
        for j in range(len(hand)):
            if hand[i] == hand[j]:
                same += 1
        if same > max_same:
            max_same = same
    return max_same

def get_max_same_card_ignore_jokers(hand):
    return get_max_same_card(hand.strip('J'))

def get_count_jokers(hand):
    jokers = 0
    for i in range(len(hand)):
        if 'J' == hand[i]:
            jokers += 1
    return jokers

def is_five_of_a_kind(hand):
    max = get_max_same_card_ignore_jokers(hand)
    jokers = get_count_jokers(hand)
    if max == 5 and jokers == 0:
        return True
    if max == 4 and jokers == 1:
        return True    
    if max == 3 and jokers == 2:
        return True        
    if max == 2 and jokers == 3:
        return True
    if max == 1 and jokers == 4:
        return True            
    elif jokers == 5: 
        return True    
    return False

def is_four_of_a_kind(hand):    
    max = get_max_same_card_ignore_jokers(hand)
    jokers = get_count_jokers(hand)
    if max == 4 and jokers == 0:
        return True
    if max == 3 and jokers == 1:
        return True    
    if max == 2 and jokers == 2:
        return True        
    if max == 1 and jokers == 3:
        return True        
    elif jokers == 4: 
        return True    
    return False

def is_distinct(hand):
    return get_max_same_card(hand) == 1

def is_full_house(hand):
    freq = check_char_freq(hand)
    max = get_max_same_card_ignore_jokers(hand)
    jokers = get_count_jokers(hand)

    #print(f"DEBUG: {freq}")
    if freq == [3,2]:
        return True
    elif jokers == 1 and freq == [2,2,1]:
        return True
    elif jokers == 2 and freq == [2,1,1,1]:
        return True    
    elif jokers == 3 and freq == [3,1,1]:
        return True        
    return False

def is_three_of_a_kind(hand):
    freq = check_char_freq(hand)
    max = get_max_same_card_ignore_jokers(hand)
    jokers = get_count_jokers(hand)

    #print(f"DEBUG: {freq}")
    if freq == [3,1,1]:
        return True
    elif jokers == 1 and freq == [2,1,1,1]:
        return True
    elif jokers == 2 and max == 1:
        return True
    return False

def is_two_pair(hand):
    freq = check_char_freq(hand)
    #print(f"DEBUG: {freq}")
    max = get_max_same_card_ignore_jokers(hand)
    jokers = get_count_jokers(hand)

    if freq == [2,2,1]:
        return True
    elif jokers == 1 and freq == [2,1,1,1]:
        return True
    elif jokers == 2 and max == 1:
        return True    
    return False


def is_one_pair(hand):
    max = get_max_same_card_ignore_jokers(hand)
    jokers = get_count_jokers(hand)

    freq = check_char_freq(hand)
    #print(f"DEBUG: {freq}")
    if [1,1,1,1] and max == 1 and jokers == 1:
        return True
    elif freq == [2,1,1,1]:
        return True
    return False



def get_hand_type(hand):
    #Five of a kind, where all five cards have the same label: AAAAA
    #Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    #Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    #Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    #Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    #One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    #High card, where all cards' labels are distinct: 23456

    if is_five_of_a_kind(hand):
        return 0

    if is_four_of_a_kind(hand):
        return 1

    if is_full_house(hand):
        return 2

    if is_three_of_a_kind(hand):
        return 3

    if is_two_pair(hand):
        return 4

    if is_one_pair(hand):
        return 5

    if is_distinct(hand): # High card
        return 6
        
    raise ValueError(f"Unhanded type for hand={hand}")



def get_card_value(label):
    if label.isnumeric():
        return int(label)

    if label == 'A':
        return 14
    if label == 'K':
        return 13
    if label == 'Q':
        return 12
    if label == 'T':
        return 10
    
    # Wildcard jokers
    if label == 'J':
        return 1

    
    raise ValueError("label={label}")
    

def compare_same_hand_type(hand_left, hand_right):
    # A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. 
    # The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

    for i in range(len(hand_left)):
        if not hand_left[i] == hand_right[i]:
            return get_card_value(hand_left[i]) - get_card_value(hand_right[i])
    return 0

def compare(hand_left, hand_right):
    # return a negative value (< 0) when the left item should be sorted before the right item
    # return a positive value (> 0) when the left item should be sorted after the right item
    # return 0 when both the left and the right item have the same weight and should be ordered "equally" without precedence

    if hand_left == hand_right:
        return 0
    
    type_hand_left = get_hand_type(hand_left)
    type_hand_right = get_hand_type(hand_right)

    if not type_hand_left == type_hand_right:
        return  type_hand_right - type_hand_left
    
    return compare_same_hand_type(hand_left, hand_right)



def sort_by_rank_with_wildcard_jokers(list_of_hands):

    #return ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA']
    sorted_list = sorted(list_of_hands, key=cmp_to_key(compare))
    #print(f"DEBUG: sorted_list = {sorted_list}")

    return sorted_list
    #return ['32T3K', 'KK677', 'T55J5', 'QQQJA', 'KTJJT']


def get_total_winnings_with_wildcard_jokers(filename):
    lines = fileutils.get_file_lines(filename)

    map_hand_to_bid = defaultdict(int)
    for l in lines:
        #print(f"DEBUG: line={l}")
        (hand, bid) = l.split()

        #print(f"DEBUG: hand={hand} bid={bid}")
        map_hand_to_bid[hand] = int(bid)

    #print(f"DEBUG: map_hand_to_bid={map_hand_to_bid}")

    sorted_hands = sort_by_rank_with_wildcard_jokers(map_hand_to_bid.keys())

    winnings = 0
    for i in range(len(sorted_hands)):
        value = (1+i) * map_hand_to_bid[sorted_hands[i]]
        #print(f"DEBUG: value={value}")
        winnings += value

    return winnings