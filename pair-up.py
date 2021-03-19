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
    as keys and random round pairs with non-repeating names as values."""

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

        while len(round_pairs) < num_of_ind / 2:
            pair_num = random.randint(0, num_of_pairs - 1)
            round_pairs.append(total_pairs.pop(pair_num))
            print("Total pairs left:", len(total_pairs))
            num_of_pairs = len(total_pairs)
            if len(round_pairs) == 4:
                round_pairs_dict[round_num] = round_pairs

        print(round_pairs_dict)


pair_up(['Rachel', 'Hunter', 'Alicia', 'Nan', 'Elizabeth', 'Ilana', 'Jen', 'Yvonne'])