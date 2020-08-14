import csv
import json
from collections import defaultdict


def createTree():
    return defaultdict(createTree)


def createLeaf(branch, leaf):
    """ Recursive function to build desired  Tree structure

    """
    if type(branch) is tuple:

        result = {"label": branch[0], "id": branch[1], "link": branch[2]}

    else:

        result = {"Base URL":branch}

    # add children node if the leaf actually has any children
    if len(leaf.keys()) > 0:

        result["children"] = [createLeaf(i, j) for i, j in leaf.items()]

    return result


def main():
    """ This is the Main Method Executed First.

    First it's parsing the csv file and builds a tree hierarchy from it.
    Second it's recursively iterating over the tree and building custom
    json-like structure (via dict).

    """
    tree = createTree()
    # NOTE: you need to have data.csv file as in your directory
    with open('data.csv') as csvfile: # Open CSV File using Context Managers
        reader = csv.reader(csvfile)
        for rowId, row in enumerate(reader): # Iterate Over the File

            # skipping first header row. remove this logic if your csv is
            # headerless
            if rowId == 0:
                continue

            # usage of python magic to construct dynamic tree structure and
            # basically grouping csv values under their parents
            leaf = tree[row[0]]
            for cid in range(1, len(row), 3):
                if len(row[cid]) > 0:
                    leaf = leaf[row[cid], row[cid + 1], row[cid + 2]]

    # building a custom tree structure
    result = []
    for id, leafVal in tree.items():
        result.append(createLeaf(id, leafVal))

    # Writing result into another json file
    response=json.dumps(result,indent=1)
    f = open('test.json', 'w')
    f.write(response)


# so let's roll
main()
