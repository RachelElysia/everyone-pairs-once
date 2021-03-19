import random

# Example:
# Input:  ['Rachel', 'Hunter', 'Alicia', 'Nan', 'Elizabeth', 'Ilana', 'Jen', 'Yvonne']
# Output Example:
# Round 1: {{'Rachel', 'Hunter'}, {'Alicia', 'Nan'}, {'Elizabeth', 'Ilana'}, {'Jen', 'Yvonne'})
# Round 2: {{'Rachel', 'Alicia'}, {'Hunter', 'Nan'}, {'Elizabeth', 'Jen'}, {'Ilana', 'Yvonne'})
# Round 3: {{'Rachel', 'Nan'}, {'Hunter', 'Alicia'}, {'Elizabeth', 'Yvonne'}, {'Ilana', 'Jen'})
# Round 4: {{'Rachel', 'Hunter'}, {'Alicia', 'Nan'}, {'Elizabeth', 'Ilana'}, {'Jen', 'Yvonne'})
# Round 5: ....
# Round 6: ....
# Round 7: .... DONE

# In the end there should be a set of sets with 7 + 6 + 5 + 4 + 3 + 2 + 1 = 28 pairings

# What to do with odd groups?

def pair_up(lst):
    """ Input a list of people and returns a dictionary with round numbers
    as keys and tournament style round-pairs with non-repeating names as values."""
    half_length = int(len(lst) / 2)

    rounds = {}

    for round_num in range(1, len(lst)):

        entire_list = lst[:1] + lst[-round_num:] + lst[1:-round_num]
        print(entire_list)

        first_half= entire_list[:half_length]
        second_half = entire_list[half_length:]
        print(first_half)
        second_half.reverse()
        print(second_half)

        rounds[round_num] = list(zip(first_half, second_half))
    
    return rounds

def print_pair_ups(lst):
    pair_up_dict = pair_up(lst)

    for key, value in pair_up_dict.items():
        print(f'Round {key} Pairs: {value}')

def pair_up_random(lst):
    """ Input a list of people and returns a dictionary with round numbers
    as keys and random round pairs with non-repeating names as values.
    
    Tried to figure out how I could make random work, and it's just unsuccessful.
    """

    num_of_ind = len(lst)
    num_of_rounds = len(lst) - 1

    total_pairs = []

    for idx, ind in enumerate(lst):
        for partner_number in range(idx+1, num_of_ind):
            total_pairs.append((ind, lst[partner_number]))

    # print("Number of Pairs:", len(total_pairs), "\n Pairs Listed:", total_pairs)

    num_of_pairs = len(total_pairs)

    round_pairs_dict = {}

    for round_num in range(1, num_of_ind):
        round_pairs =  []
        round_list = lst.copy()

        counter = 0

        while len(round_pairs) < num_of_ind / 2:
            pair_num = random.randint(0, num_of_pairs - 1)

            potential_pair = total_pairs[pair_num]

            if potential_pair[0] in round_list and potential_pair[1] in round_list:
                round_list.remove(potential_pair[0])
                round_list.remove(potential_pair[1])
                round_pairs.append(total_pairs.pop(pair_num))

                print("Total pairs left:", len(total_pairs))
                num_of_pairs = len(total_pairs)
                if len(round_pairs) == 4:
                    round_pairs_dict[round_num] = round_pairs

        print(round_pairs_dict)
        round_list = lst
    
    if len(round_pairs_dict) == num_of_rounds:
        return "Success!!!! This is it!"
    else:
        return pair_up_random(lst)



# Test
# pair_up(['Rachel', 'Hunter', 'Alicia', 'Nan', 'Elizabeth', 'Ilana', 'Jen', 'Yvonne'])

# pair_up([1, 2, 3, 4, 5, 6, 7, 8])

print_pair_ups(['Rachel', 'Hunter', 'Alicia', 'Nan', 'Elizabeth', 'Ilana', 'Jen', 'Yvonne'])

