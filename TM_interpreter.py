# Carnegie Mellon University 15-251 Great Ideas in Theoretical Computer Science
# Homework 3 Programming Assignment
# Starter code for TM_interpreter 
# TODO Implement the Turing Machine Interpreter

from TM_classes import State, Configuration, TuringMachine, Result
    
def TM_interpret(M, x, k = None):
    """TODO implement function that simulates TM M on input x. A Universal TM!

    Inputs: 
        - M: TuringMachine
        - x: str is the string representing the input to the TM
        - k: int is an optional parameter used if we want to simulate the TM for maximum of k steps (inclusive)
    Returns: tuple containing two elements
        - list of Configuration corresponding to the configuration of the TM at each timestep (including the initial configuration)
        - Result of ACCEPT, REJECT, or UNDETERMINED based on the behavior of the TM on input x
    Note:
        - If M is not a valid encoding of a TM, then we reject, with `None` as our list of configurations
        - If k is not set and TM loops forever, this function should loop forever as well
    """
    if not validate_TM(M): return (None, Result.REJECT) # First, check that the input TM is a correct encoding.

    #TODO: What should the initial configuration be?
    config = Configuration(None, None, None) 
    
    while True:
        config = simulate_step(M, config)
        # TODO fill in the rest of this loop
        # When do we know to Accept or Reject?
        # If k is set, when do we return "Undetermined after k steps"?
        # Remember to keep track of the configuration at each time step!

        # Finally, remember that each step corresponds to an application of
        # the transition function. If k = 3, we allow three applications of
        # the transition function. See the provided test cases for exact
        # details.

def validate_TM(M):
    """TODO Determine if the TM is correctly defined.
    
    Assume that the types of given parameters are correct (ex. Q is a set containing State objects, etc).
    Here are some things that you should check:
        - does Q contain q0, q_acc, and q_rej
        - is the input alphabet a subset of the tape alphabet?
        - etc (determine the other things you should check)
    Return True if the input TM is a valid encoding, False otherwise.
    """
    return False
          
def simulate_step(M, config):
    """TODO this is a helper function used by interpret to simulate one step of the TM.

    This is optional, but will be helpful in writing the TM interpreter.

    Given the current configuration, we want to compute and return the next configuration.
    """
    u, q, v = config.u, config.q, config.v # current configuration

    # TODO compute the next configuration!
    u_new, q_new, v_new = None, None, None

    return Configuration(u_new, q_new, v_new) # return next configuration
