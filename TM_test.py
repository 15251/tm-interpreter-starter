# Carnegie Mellon University 15-251 Great Ideas in Theoretical Computer Science
# Homework 3 Programming Assignment
# Sample test file - you can make your own tests, or even run your examples!

from TM_classes import State, Configuration, TuringMachine, Result
from TM_interpreter import TM_interpret, validate_TM

def config_normalize(config):
    return Configuration(u=config.u.lstrip("_"), q=config.q, v=config.v.rstrip("_"))

def config_equal(config1, config2):
    return config_normalize(config1) == config_normalize(config2)

def check_configs(reference, actual):
    assert len(reference) == len(actual), "Number of configurations do not match"
    for i in range(len(reference)):
        assert config_equal(reference[i], actual[i]), "Configuration at time step " + str(i) + " do not match"

def ExampleTest():
    Q = set([State(name) for name in ["q0", "q1", "q_acc", "q_rej"]]) # Q = {q0, q1, q_acc, q_rej}
    Sigma = set(['0', '1']) # our input alphabet is {0, 1}
    Gamma = set(['0', '1', '_']) # our tape alphabet is {0, 1, _(blank)}
    delta = { # delta: Q \ {q_acc, q_rej} x Gamma -> Q x Gamma x {'L', 'R'}
        (State("q0"), '0'): (State("q1"), '0', 'R'),
        (State("q0"), '1'): (State("q1"), '1', 'R'),
        (State("q0"), '_'): (State("q_acc"), '1', 'R'),
        (State("q1"), '0'): (State("q0"), '0', 'R'),
        (State("q1"), '1'): (State("q0"), '1', 'R'),
        (State("q1"), '_'): (State("q_rej"), '1', 'R')
    }
    q0 = State("q0") # initial state is "q0"
    q_acc = State("q_acc") # accepting state is "q_acc"
    q_rej = State("q_rej") # rejecting state is "q_rej"
    M = TuringMachine(Q, Sigma, Gamma, delta, q0, q_acc, q_rej)

    # Test ""
    configs, output = TM_interpret(M, "")
    assert output == Result.ACCEPT, "TM should accept empty string"
    check_configs([Configuration("", q0, ""),
                   Configuration("1", q_acc, "")], configs)
    print("Test passed for empty string")

    # Test "01"
    configs, output = TM_interpret(M, "01")
    assert output == Result.ACCEPT, "TM should accept string 01"
    check_configs([Configuration("", State("q0"), "01"), 
                   Configuration("0", State("q1"), "1"),
                   Configuration("01", State("q0"), ""),
                   Configuration("011", State("q_acc"), "")], configs)
    print("Test passed for string 01")

    # Test "0101011"
    configs, output = TM_interpret(M, "0101011")
    assert output == Result.REJECT, "TM should reject string 0101011"
    check_configs([Configuration("", State("q0"), "0101011"), 
                   Configuration("0", State("q1"), "101011"),
                   Configuration("01", State("q0"), "01011"), 
                   Configuration("010", State("q1"), "1011"),
                   Configuration("0101", State("q0"), "011"), 
                   Configuration("01010", State("q1"), "11"),
                   Configuration("010101", State("q0"), "1"), 
                   Configuration("0101011", State("q1"), ""),
                   Configuration("01010111", State("q_rej"), "")], configs)
    print("Test passed for string 0101011")

    # Test "0101011", k = 5
    configs, output = TM_interpret(M, "0101011", 5)
    assert output == Result.UNDETERMINED, "TM is undetermined after 5 steps on 0101011"
    check_configs([Configuration("", State("q0"), "0101011"), 
                   Configuration("0", State("q1"), "101011"),
                   Configuration("01", State("q0"), "01011"), 
                   Configuration("010", State("q1"), "1011"),
                   Configuration("0101", State("q0"), "011"), 
                   Configuration("01010", State("q1"), "11")], configs)
    # Note: there are **6** entries in the configuration list here, even though
    # k = 5. Why do you think that is?

    print("Test passed for string 0101011 and k = 5")

def ExampleInvalidTMTest():
    Q = set([State(name) for name in ["q1", "q_acc", "q_rej"]])
    Sigma = set(['0', '1']) # our alphabet is {0, 1}
    Gamma = set(['0', '1', '_']) # our tape alphabet is {0, 1, _(blank)}
    delta = {
        (State("q0"), '0'): (State("q1"), '0', 'R'),
        (State("q0"), '1'): (State("q1"), '1', 'R'),
        (State("q0"), '_'): (State("q_acc"), '1', 'R'),
        (State("q1"), '0'): (State("q0"), '0', 'R'),
        (State("q1"), '1'): (State("q0"), '1', 'R'),
        (State("q1"), '_'): (State("q_rej"), '1', 'R')
    }
    q0 = State("q0")
    q_acc = State("q_acc")
    q_rej = State("q_rej")
    M = TuringMachine(Q, Sigma, Gamma, delta, q0, q_acc, q_rej)
    assert (not validate_TM(M)), "This TM is invalid. Can you see why?"
    _, output = TM_interpret(M, "")
    assert output == Result.REJECT, "Invalid TM should be rejected"
    print("Test passed for invalid TM")

ExampleTest()
ExampleInvalidTMTest()
