# link https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter


def calculadora(lista, resultado):
    
    # len validation
    if len(lista) > 5:
        print("Error: Too many problems.")
        exit()
    
    # Validation of operators
    for x in lista:
        if x.find("*") != -1 or x.find("/") != -1:
            print("Error: Operator must be '+' or '-'.")
            exit()
  
    for x in lista:
        # String slicing and validation of integers
        
        try:

            int(x[:breakpoint])
            int(x[breakpoint+1:])
            if len(x[:breakpoint]) > 4 or len(x[breakpoint+1:]) > 4:
                print("Error: Numbers cannot be more than four digits.")
                exit()
        except ValueError:
            print("Error: Numbers must only contain digits.")
            exit()
        
        if breakpoint != -1:
            operation = int(x[:breakpoint])+ int(x[breakpoint+1:])
            if resultado:
                result = operation
            else:
                result = ""
                # display
            print(f"""\n\n\n    {x[:breakpoint]}    
{x[breakpoint]}
    {x[breakpoint+1:]}
--------------------
    {result}""")
            
            
        else:
            breakpoint = x.find("-")
            operation = int(x[:breakpoint]) - int(x[breakpoint+1:])
            if resultado:
                result = operation
            else:
                result = ""
                # display
            print(f"""\n\n\n    {x[:breakpoint]}    
{x[breakpoint]}
    {x[breakpoint+1:]}
--------------------
    {result}""")
        
        
    

        
  
        



# operaciones = ["100-20"]













# calculadora(operaciones,True)
