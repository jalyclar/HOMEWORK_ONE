#!/opt/anaconda3/bin/python

import sys 
import numpy as np
import matplotlib.pyplot as plt 
from astropy.io import ascii
import os 
import pandas as pd


#                 TO DO:   Change dpi in generate_plot, Create MakeFile ,Document class and functions 


class homework_one:
    """
    Parameters:
    ------------
    
    Attributes:
    ------------

    Methods:
    ------------

    """

    def __init__(self):
        self.function=None 
        self.filename=None
        self.read_from_file=None 
        self.print=None
        self.x=np.arange(-10,10,0.05)
        self.y_values={} 
        self.table_df=pd.DataFrame
        
    def parse_argv(self): #Parsing over command line arguments
        """
        Parameters:
        ------------

        Returns:
        ------------
        """
        for argument in sys.argv[1:]: #Skips over 1st argument (script name)
            if argument.startswith("--function="): #Assigns after = 
                self.function=argument.split("=")[1]
            if argument.startswith("--write="):
                self.filename=argument.split("=")[1]
            if argument.startswith("--read_from_file="):
                self.read_from_file=argument.split("=")[1]
            if argument.startswith("--print="):
                self.print=argument.split("=")[1]
 
    def plot_func(self): #Plotting data from function(s) provided
        """
        Parameters:
        ------------

        Returns:
        ------------
        """  
        if self.function==None:  
            print('Error: A function argument needs to be provided.')
            quit() #exits out script 
    
        functions=self.function.split(",") #Seperates multiples func if given 
        for func in functions:
            if func == "cos":
                y=np.cos(self.x)
            elif func == "sin":
                y=np.sin(self.x)
            elif func == "sinc":
                y=np.sinc(self.x)
            else:
                print(f"Error: Function '{func}' is not understood.")
                quit()
            self.y_values[func]=y #stores y values and corresponding func in dict
            label=f'{func}(x)' 
            plt.plot(self.x,y,label=label)

        plt.title(f"Plot of {', '.join([f'{f}(x)' for f in functions])}")
        plt.xlabel("x values")
        plt.ylabel(f"{', '.join([f'{f}(x)' for f in functions])}")
        plt.legend()
        plt.show()
    
    def write_file(self):
        """
        Parameters:
        ------------

        Returns:
        ------------
        """ 
        if self.filename==None:
            pass #Does nothing if no argument is given 
        else:
            if self.y_values is None:
                print("Error: No y values to put in table.") #If self.y_values werent passed correctly 
            data=[self.x] + [self.y_values[func].tolist() for func in self.y_values] #___.write only takes lists or np.array as argument
            names=['x']+ [f'{func}(x)' for func in self.y_values] #list of headers 
            
            dir=os.path.dirname(os.getcwd()) #Stores in the directory above the local repository clone
            file_path=os.path.join(dir,self.filename)

            ascii.write(data, file_path, names=names, overwrite=True) #Allows file to be overwritten 
            print(f'Data written to {file_path}')

    def read_file(self):
        """
        Parameters:
        ------------

        Returns:
        ------------
        """ 
        if self.read_from_file==None:
            pass #Does nothing if no argument is given
        else:
            dir=os.path.dirname(os.getcwd()) #Reads from directory above the local repository clone
            file_path=os.path.join(dir,self.read_from_file)
            self.table_df=pd.read_csv(file_path,delimiter=' ')
            print(self.table_df) #Comment out for final commit

    def generate_plot(self):
        """
        Parameters:
        ------------

        Returns:
        ------------
        """
        if self.print==None: #Does nothing if no argument is supplied 
            pass
        else:
            x=self.table_df.iloc[:,0] #x values assigned as first column in df
            for col in self.table_df.columns[1:]: 
                y=self.table_df[col] #y values assigned as each column after first 
                plt.plot(x,y,label=col)
            plt.title(f"Plot of {', '.join([f'{col}' for col in self.table_df.columns[1:]])}") 
            plt.xlabel("x values")
            plt.ylabel(f"{', '.join([f'{col}' for col in self.table_df.columns[1:]])}")
            plt.legend()

            format=self.print.split(",") #Splits provided arguments if multiple 
            dir=os.path.dirname(os.getcwd()) #Gets dir path of directory above the local repsoitroy clone 
            name='exampleplot.' #Name given to file(s) that will have a plot
            for option in format:
                if option=='jpeg':
                    full=''.join([name,option])#joins together filename and format provided 
                    plt.savefig(os.path.join(dir,full)) #Saves figure to the directory above the local repsotiory clone 
                elif option=='eps':
                    full=''.join([name,option])
                    plt.savefig(os.path.join(dir,full))
                elif option=='pdf':
                    full=''.join([name,option])
                    plt.savefig(os.path.join(dir,full))
                else:
                    print(f'Error: {option} not understood')
                    continue #Keeps going through provided arguments (if multiple)
            print(f"Plots saved as 'exampleplot' in the following formats: {[option for option in format]}") #Lists all the formats its saved as
            plt.show() #comment out for final commit 

if __name__ == "__main__": #To run as script  
    data=homework_one() #To call each function within the class  
    data.parse_argv()
    data.plot_func()
    data.write_file()
    data.read_file()
    data.generate_plot()