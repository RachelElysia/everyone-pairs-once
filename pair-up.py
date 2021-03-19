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