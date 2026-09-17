# Carnegie Mellon University 15-251 Great Ideas in Theoretical Computer Science
# Homework 3 Programming Assignment
# Starter code for TM_examples
# TODO Define a TuringMachine object that solves the given problems

from TM_classes import State, TuringMachine

def TM1():
    """Define and then return a Turing Machine with the following behavior:

    Input alphabet is {0, 1}. 
    The tape alphabet is a superset of {0, 1, _}, where _ is the blank symbol.
    (It is up to you if you want the tape alphabet to contain more symbols.)
    If the input has equal number of 0s and 1s, accept.
    Otherwise, reject.
    """
    pass

def TM2():
    """Define and then return a Turing Machine with the following behavior:

    Input alphabet is {0, 1}.
    The tape alphabet is a superset of {0, 1, _}, where _ is the blank symbol.
    (It is up to you if you want the tape alphabet to contain more symbols.)
    If the input does not correspond to the usual binary encoding of a natural number,
    output the empty string.
    Otherwise, output x + 1 in binary, where x is the input number.
    """
    pass

def Bonus():
    """Define and then return a Turing Machine with the following behavior: (BONUS)

    Input alphabet is {0, 1, $}.
    The tape alphabet is a superset of {0, 1, $, _}, where _ is the blank symbol.
    (It is up to you if you want the tape alphabet to contain more symbols.)
    If the input is not of form x$y where x and y are binary encodings of natural numbers,
    output the empty string.
    Otherwise, output the sum of x and y in binary.
    """
    pass