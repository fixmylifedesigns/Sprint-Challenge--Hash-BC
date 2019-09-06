#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    results = []
    hashtable= {}

    # if on the length of weights is 1 or none it returns none
    if len(weights) <= 1:
        return None

    for x in range(0,len(weights)):
        # creates a new element that comes from subtracting the limit and weight
        new = limit - weights[x]
        # adds that new element to the table
        hashtable[weights[x]] = new

    for y in range(0, len(weights)):
        if limit - weights[y] in hashtable:
            results.insert(0, y)
    return results
        


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " ))
    else:
        print("None")


weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
print(get_indices_of_item_weights(weights_4, 9, 7))
