import sys 
import numpy as np
import matplotlib.pyplot as plt 

#Parsing over command line arguments 
def parse_arguments():
    function=None
    write=None 
    read_from_file=None 
    print=None
    for argument in sys.agrv:
        if argument.startswith("--function="): #Assigns after = 
            function=argument.split("=")[1]
        if argument.startswith("--write="):
            write=argument.split("=")[1]
        if argument.startswith("--read_from_file="):
            read_from_file=argument.split("=")[1]
        if argument.startswith("--print="):
            print=argument.split("=")[1]
    return function, write, read_from_file, print
 
def plot_func(function):
    x=np.arange(-10,10,0.05)
    
    functions=function.split(",") #Seperates multiples func if given 
    for func in functions:
        if func == "cos":
            y=np.cos(x)
        elif func == "sin":
            y=np.sin(x)
        elif func == "sinc":
            y=np.sinc(x)
        else:
            print(f"Function {func} is not understood.")
            continue #Skips over bad inputs 
        plt.plot(x,y,label=func)

    plt.title(f"Plot of {' (x),  (x)'.join([f'{f}(x)' for f in functions])}")
    plt.xlabel("x values")
    plt.ylabel(f"{' (x),  (x)'.join([f'{f}(x)' for f in functions])}")
    plt.legend()
    plt.show()

    