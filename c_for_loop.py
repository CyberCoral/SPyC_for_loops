###
### Name of project: SPyC_for_loops
###
### Author: CyberCoral
###
### Description of project: It's an implementation of 
###                         C for loops, with lambda 
###                         functions and dictionaries.
###
### Date of start of project: 19 / 01 / 2025
###
### End of current version of project: 19 / 01 / 2025
###
### Version: 1.0
###
### -----------------------------------
###
### Github page: https://github.com/CyberCoral
###
### Repository page: https://github.com/CyberCoral/SPyC_for_loops/
###
### Youtube channel: https://www.youtube.com/@9Coral
###

###
### for loop in C
###
### for (<index variable>; <exit clause>; <incremental>)
###

def PythonExample() -> int:
    '''
    An explanation on the
    features of 
    "for" and "while" loops 
    in Python3.
    '''
    
    # for loop
    
    # i is the index variable
    # exit clause is not explicit
    # incremental is not explicit
    
    # for i in (<collection> | <range> | <map?>)
    
    # Conclusion: "while" loop would fit best into it
    
    
    # while loop
    
    # 1a. We can add as many index variables as we want.
    # 1b. The index variables must be defined prior to the
    # loop, unless you use narwhal operator (:=).
    
    # 2. Exit clause is explicit (*)
    
    # 3. Incremental can be stated inside the loop.
    
    # while i := -1 > 0: # *: Exit clause is explicit
    
    return 0


def C_for_loop():
    '''
    A sketch of what a
    C-styled for loop would
    look like.
    '''
    
    # 1st. Index variables ( i )
    i = 0
    
    while not (i > 5): # 2nd. Exit clause ( i > 5 )
        
        print(i) # Code
        
        i += 1 # 3rd. Incremental
        
        
def Custom_C_for_loop(used_variables: dict = {"i":0}, exit_clause = lambda x: True if x <= 5 else False, incremental = lambda y: -~y, *, code: list = [((0,) ,lambda z: print(z), False)]):
    '''
    A way of making 
    C-like for loops.
    
    "variables" is a dict
    with strings as keys.
    
    "exit_clause" is a lambda
    function that must only
    return either True or False,
    based on input.
    
    "incremental" is a lambda
    function that takes some
    input and "increments" it 
    (it should prevent
     infinite loops).
    
    "code" is a tuple that
    contains:
    1. A tuple with int numbers,
    the variables' index.
    2. A lambda
    function that takes
    some input (optional)
    and does an action.
    3. A bool value,
    which if True means the
    lambda function's value
    must be stored in variables.
    If False, the lambda function's
    output is not stored.
    '''
    
    variables = {k:v for k,v in used_variables.items()}
    
    # Checks for variables:
    if [isinstance(i, str) for i in list(variables.keys())].count(False) != 0:
        raise TypeError("The keys must be strings.")
    
    # Checks for code:
    if not isinstance(code, list):
        raise TypeError("The code is not a list.")
    elif [isinstance(i, tuple) for i in code].count(False) != 0:
        raise TypeError("The elements in code must be tuples.")
    
    for code_part in code:
        if len(code_part) != 3:
            raise IndexError("The code tuple does not have two elements.")
        
        elif not isinstance(code_part[0], tuple):
            raise IndexError("The index part of the code is not a tuple.")
        elif [isinstance(i, int) for i in code_part[0]].count(False) != 0:
            raise TypeError("The elements in the index part of the code must be positive integers (including 0).")
        elif [i >= 0 for i in code_part[0]].count(False) != 0:
            raise ValueError("The numbers on the index part of the code must be positive integers (including 0).")
        elif [code_part[0][i] < len(list(variables.keys())) for i in range(len(code_part[0]))].count(False) != 0:
            raise IndexError("The indexes' numbers are greater than the number of available variables.")
        
        elif not isinstance(code_part[2], bool):
            raise TypeError("This value must be a bool.")
            
        # Checks if there are enough variables for code.
        elif code_part[1].__code__.co_argcount > len(list(variables.keys())): 
            raise IndexError("There are not enough variables for code.")
        
        # Checks if there are enough variables on the index part of code to be used in code.
        elif code_part[1].__code__.co_argcount != len(code_part[0]):
            raise IndexError("There are not enough variables for code to use them.")
       
        # Checks if code[1] is callable
        try:
            code_part[1].__code__.co_argcount
        except TypeError:
            raise TypeError("The lambda function part of code must be callable.")
        
        
    # Checks if there are the same number of variables on the exit clause and on variables.
    if len(list(variables.keys())) < exit_clause.__code__.co_argcount:
        raise IndexError("There are not enough variables for the exit clause.")
        
      
    # Checks for argument count on the exit clause and incremental.
    if exit_clause.__code__.co_argcount != incremental.__code__.co_argcount:
        raise IndexError("There must be equal number of arguments between exit_clause and incremental.") 
    
    # The C-like for loop part:
    while exit_clause(*list(variables.values())[:exit_clause.__code__.co_argcount]): # Exit clause.
        
        for code_part in code:
            # The variables that are going to be used.    
            used_vars = [list(variables.keys())[i] for i in code_part[0]]
            code_vals = [variables[i] for i in used_vars]
            
            # Code part
            if code_part[2]:
                # The variable which will store the result from code.
                store_val = [list(variables.keys())[code_part[0][0]], 0]
                store_val[1] = code_part[1](*code_vals)
                variables.update({store_val[0]:store_val[1]})
            
            else:
                # The variables are used on the code part.
                code_part[1](*code_vals)
            
        # Incremental part.    
        indexes_key = [list(variables.keys())[i] for i in range(exit_clause.__code__.co_argcount)]
        indexes_val = [variables[i] for i in indexes_key]
        
        index = incremental(*indexes_val)
        variables.update({indexes_key[0]:index})
            
    if [code_part[2] for code_part in code].count(True) > 0:
        return variables
    return None        
        
