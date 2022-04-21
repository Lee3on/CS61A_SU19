""" Optional questions for Lab 05 """

from lab05 import *

# Shakespeare and Dictionaries


def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev in table:
            table[prev].append(word)
        if prev not in table:
            table[prev] = [word]
        prev = word
    return table


def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        "*** YOUR CODE HERE ***"
        result += word + ' '
        word = table[word][random.randint(0, len(table[word]) - 1)]
    return result.strip() + word


# table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
# print(construct_sent('Wow', table))
# print(construct_sent('Sentences', table))


def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
# tokens = shakespeare_tokens()
# table = build_successors_table(tokens)


def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)


def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    lst = []
    for val in vals:
        lst.append(tree(val))
    if is_leaf(t):
        return tree(label(t), lst)

    new_branches = []
    for branch in branches(t):
        new_branches += [sprout_leaves(branch, vals)]
    return tree(label(t), new_branches)


# t1 = tree(1, [tree(2), tree(3)])
# new1 = sprout_leaves(t1, [4, 5])
# print_tree(new1)
# t2 = tree(1, [tree(2, [tree(3)])])
# new2 = sprout_leaves(t2, [6, 1, 2])
# print_tree(new2)


def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t1) and is_leaf(t2):
        return tree(label(t1) + label(t2))
    if is_leaf(t1):
        return tree(label(t1) + label(t2), branches(t2))
    if is_leaf(t2):
        return tree(label(t1) + label(t2), branches(t1))

    new_branches = []
    br_t1 = branches(t1)
    br_t2 = branches(t2)
    l1 = len(br_t1)
    l2 = len(br_t2)
    if l1 < l2:
        for i in range(l1):
            new_branches += [add_trees(br_t1[i], br_t2[i])]
        new_branches += br_t2[l1:]
        return tree(label(t1) + label(t2), new_branches)
    if l1 > l2:
        for i in range(l2):
            new_branches += [add_trees(br_t1[i], br_t2[i])]
        new_branches += br_t1[l2:]
        return tree(label(t1) + label(t2), new_branches)

    for i in range(l1):
        new_branches += [add_trees(br_t1[i], br_t2[i])]
    return tree(label(t1) + label(t2), new_branches)


# print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
# print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
# print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]),
#                      tree(2, [tree(3, [tree(4)]), tree(5)])))
# numbers = tree(1,
#                [tree(2,
#                      [tree(3),
#                       tree(4)]),
#                 tree(5,
#                      [tree(6,
#                            [tree(7)]),
#                       tree(8)])])
# print_tree(add_trees(numbers, numbers))
