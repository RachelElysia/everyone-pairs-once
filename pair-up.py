# Inspiration:
# My bootcamp experience was being re-paired with the samebpeople several times
# and never had the opportunities to code with others.

# Relation to teaching:
# Students choose their friends,
# Teachers choose heterogeneous or homogenous pairs.

# Potential solution:
# This is random pairs with no repetition!

# Given a list of names, names are returned each round as pairs.
# Each pair is only shown once.

# Pairs will be kept in a set as to not be repeated.
# If pairs are already in a set, the algorithm will reroll.

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
    num_of_ind = len(lst)
    num_of_rounds = len(lst) - 1

    total_pairs = []

    for idx, ind in enumerate(lst):
        for partner_number in range(idx+1, num_of_ind):
            total_pairs.append((ind, lst[partner_number]))
    
    print("Number of Pairs:", len(total_pairs), "\n Pairs Listed:", total_pairs)

    for round_num in range(1, num_of_ind):

        print("Round:", round_num)


pair_up(['Rachel', 'Hunter', 'Alicia', 'Nan', 'Elizabeth', 'Ilana', 'Jen', 'Yvonne'])