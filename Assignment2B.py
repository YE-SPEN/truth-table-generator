# Assignment2A.py
# Purpose: define 5 functions to represent truth relationships

# Author: Eric Spensieri
# Date: October, 13 2022

def main():

    # declare value sets for error handling
    isResult = ["T", "F"]
    inError = "F"
    valueSet = list()

    print()
    print("Welcome to Assignment 2A!")

    # print instructions for user to enter statement in correct format
    print("Please consult the legend below before continuing")
    print()
    print("LEGEND")
    print("======")
    print("Type P1, P2, P3.... etc. for all variables")
    print("Type AND to represent a conjunction")
    print("Type OR to represent a disjunction")
    print("Type NOT to represent a negation")
    print("Type THEN to represent an implication")
    print("Type WITH to represent a biconditional relation")
    print("Add a space between each variable or operator")
    print("Insert parentheses () where needed")
    print()
    print("Example: ((P1 AND P2) OR (P3 AND T)) OR ((NOT P1 AND NOT P3) AND P2)")
    print()

    inError = "T"
    while inError == "T":

        # read logical statement from user
        statement = input("Please enter your propositional statement: ")
        valueSet.clear()

        # extract unique P values from entered logical sentence to determine the number of unique variables
        for i in (i + 1 for i in range(len(statement))):
            if ("P" + str(i)) in statement:
                valueSet.append("P" + str(i))

        # add delimiter spaces between parentheses
        statement = statement.replace("(", "( ")
        statement = statement.replace(")", " )")

        # split statement into set for evaluation
        statementAsSet = statement.split()

        if isValid(statementAsSet, valueSet) == "T":
            inError = "F"

        else:
            print("INPUT ERROR: Read the legend above and try again")
            continue

    # read truth values for each variable from the user and store in a list
    truthSet = list()
    for i in range(len(valueSet)):
        truthSet.append(input("Please input the truth value for " + valueSet[i] + " using T for True, F for False: "))

        # catch error for lowercase entry
        truthSet[i] = truthSet[i].replace("t", "T")
        truthSet[i] = truthSet[i].replace("f", "F")

        # catch input errors for all entries not included in result set
        inError = "T"
        while inError == "T":
            if truthSet[i] not in isResult:
                truthSet[i] = input("INPUT ERROR: Please enter either T for True or F for False: ")

                # catch error for lowercase entry
                truthSet[i] = truthSet[i].replace("t", "T")
                truthSet[i] = truthSet[i].replace("f", "F")
            else:
                inError = "F"

    # replace all values in logical statement with their corresponding truth values
    truthStatement = statement
    for i in range(len(truthSet)):
        truthStatement = truthStatement.replace(str(valueSet[i]), str(truthSet[i]))

    print()
    print("RESULTS")
    print("=======")
    print("For the entered logical statement: " + statement)
    print("With associated truth values: " + truthStatement)

    # split statement into a set for evaluation using compute method
    statementAsSet = truthStatement.split()

    print("The result is " + compute(statementAsSet))

# define negation function
def negation(entry1):
    if entry1 == "T":
        return "F"
    else:
        return "T"

# define conjunction function, returns true if both entries are true
def conjunction(entry1, entry2):
    if entry1 == entry2 == "T":
        return "T"
    else:
        return "F"

# define disjunction function, returns true if either entry is true
def disjunction(entry1, entry2):
    if entry1 == entry2 == "F":
        return "F"
    else:
        return "T"

# define implication function, only returns false if first entry is true and second is false
def implication(entry1, entry2):
    if entry1 != entry2:
        if entry1 == "T":
            return "F"
        else:
            return "T"
    else:
        return "T"

# define biconditional function, returns true if both values are equal
def biconditional(entry1, entry2):
    if entry1 == entry2:
        return "T"
    else:
        return "F"

# define function to validate each element in given logical sentence
def isValid(set, variableSet):

    isValid = ["AND", "OR", "THEN", "WITH", "NOT", "(", ")", "T", "F"]

    for i in range(len(set)):
        element = set[i]
        if (element not in isValid) and (element not in variableSet):
            return "F"

    return "T"

# define compute function
def compute(queue):
    isResult = ["T", "F"]

    # continue processing statement until final result is reached
    while len(queue) > 1:

        # pop element from queue for evaluation
        element = queue.pop(0)

        # if popped element is T, F or a close parenthesis, immediately enqueue
        if (element in isResult) or (element == ')'):
            queue.append(element)
            continue

        # if popped element is an open parenthesis, check if the next element is enclosed by a close parenthesis
        if element == '(':

            # if true, delete close parenthesis and discard popped element, otherwise enqueue
            if queue[1] == ')':
                del queue[1]
                continue
            else:
                queue.append(element)
                continue

        # if popped element is keyword NOT, check if next element is T or F
        if element == 'NOT':

            # if true, compute negation of next element, delete next element and enqueue result
            if queue[0] in isResult:
                element = negation(queue[0])
                del queue[0]
                queue.append(element)
                continue
            else:
                queue.append(element)
                continue

        # if popped element is keyword AND, check if left and right pointers are both T or F
        if element == 'AND':

            # if true, compute conjunction, delete left and right pointers, and enqueue result
            if (queue[0] in isResult) and (queue[len(queue)-1] in isResult):
                element = conjunction(queue[0], queue[len(queue)-1])
                del queue[0]
                del queue[len(queue)-1]
                queue.append(element)
                continue
            else:
                queue.append(element)
                continue

        # if popped element is keyword OR, check if left and right pointers are both T or F
        if element == 'OR':

            # if true, compute disjunction, delete left and right pointers, and enqueue result
            if (queue[0] in isResult) and (queue[len(queue)-1] in isResult):
                element = disjunction(queue[0], queue[len(queue)-1])
                del queue[0]
                del queue[len(queue)-1]
                queue.append(element)
                continue
            else:
                queue.append(element)
                continue

        # if popped element is keyword THEN, check if left and right pointers are both T or F
        if element == 'THEN':

            # if true, compute implication, delete left and right pointers, and enqueue result
            if (queue[0] in isResult) and (queue[len(queue)-1] in isResult):
                element = implication(queue[len(queue)-1], queue[0])
                del queue[0]
                del queue[len(queue)-1]
                queue.append(element)
                continue
            else:
                queue.append(element)
                continue

        # if popped element is keyword WITH, check if left and right pointers are both T or F
        if element == 'WITH':

            # if true, compute biconditional, delete left and right pointers, and enqueue result
            if (queue[0] in isResult) and (queue[len(queue)-1] in isResult):
                element = biconditional(queue[0], queue[len(queue)-1])
                del queue[0]
                del queue[len(queue)-1]
                queue.append(element)
                continue
            else:
                queue.append(element)
                continue

    # return final result
    return queue[0]

if __name__ == "__main__":
    main()

