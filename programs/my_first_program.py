from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Alice")
    party2 = Party(name="Bob")
    
    # Define secret integers as inputs
    my_int1_party1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2_party2 = SecretInteger(Input(name="my_int2", party=party2))
    
    # Perform addition of secret integers
    result = my_int1_party1 + my_int2_party2
    
    # Define the output based on the result of your computation
    output = Output(result, "sum_output", party1, party2)
    
    return [output]
