"""
TODO
    1. Upon instantiation, this class should immediately generate a 
    2. Either build methods as async tasks or build them as threads called by the dialogueLoop which would be a text processor where each dialogue line is a thread.
    3. Under Dialogue, after a dialogue line is processed a series of tasks should go into gear: clean and classify the text into manageable orders (the file names are the classes - at the start this can be hardcoded as a list of words/expressions) after which the orders should be sent to the threader and the appropriate functions should be called so as to satisfy the requests.
    4. Make a function that takes in dialogue, does some text classification into a class where a class is an available function - data should be generated on the fly.
"""

# Deal pip dependencies
# import install_dependencies
# install_dependencies.mass_install()

# Local imports currently in use ---------------------------------------------------- v
import pandas as pd
from pprint import pprint as pp
# Local imports currently in use ---------------------------------------------------- ^

# Local imports currently NOT in use ------------------------------------------------ v
# import asyncio
# import nltk
# Local imports currently NOT in use ------------------------------------------------ ^

class SmartD:
    def __init__(self, df):
        self.df = df
        self.known_information = ["means", "modes", "medians", "value_counts"]
        # self.means, self.modes, self.medians, self.value_counts = self.dataDiagnostics()
        self.dialogue = self.dialogue()
        # self.threadController = self.Dialogue()        

    # def dataDiagnostics(self):
    #     means, modes, medians, value_counts = {}, {}, {}, {}

    #     for col in self.df.columns:
    #         value_counts[col] = self.df[col].value_counts()
    #         modes[col] = self.df[col].mode()
    #         if pd.api.types.is_numeric_dtype(self.df[col]):
    #             means[col] = self.df[col].mean()
    #             medians[col] = self.df[col].median()
    #         else:
    #             means[col] = "Not numeric"
    #             medians[col] = "Not numeric"

    #     print("### MEANS ###")     
    #     pp(means)

    #     print("### MEDIANS ###")     
    #     pp(medians)

    #     print("### MODES ###")     
    #     pp(modes)

    #     print(self.df.describe())

    #     return means, modes, medians, value_counts

    def means(self):
        dic = {}
        for col in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                dic[col] = self.df[col].mean()
            else:
                dic[col] = "Not numeric"

        print("### MEANS ###")
        return dic
    
    def medians(self):
        dic = {}
        for col in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                dic[col] = self.df[col].median()
            else:
                dic[col] = "Not numeric"

        print("### MEDIANS ###")
        return dic

    def modes(self):
        dic = {}
        for col in self.df.columns:
            dic[col] = self.df[col].mode()

        print("### MODES ###")
        return dic

    def value_counts(self):
        dic = {}
        for col in self.df.columns:
            dic[col] = self.df[col].value_counts()

        print("### VALUE COUNTS ###")
        return dic

    def dialogue(self):
        while(True):
            print("\n\n")
            line = input("You: ")
            if line in dir(self): # dir(self) is the list of methods from the class
                pp(getattr(self, line)()) # searches for whatever value is in the var "line" in the list of methods of the class and runs it.
            else:
                print("I do not understand! try:", self.known_information)

    """
        TODO 2,3 ------------------------------------------------------------------------------------------------------------- V
    """
    # --------------------- DIALOGUE NLP PROCESSING --------------------- V

    # class Dialogue:
    #     async def dialogue():
    #         while(True):
    #             line = input("You:")

    #     async def threader(taskList):
    #         """Head thread controller kickstarts threads after processing dialogue line.

    #         Args:
    #             taskList (list of methods): This is a list of tasks. 
    #         """
    #         for task in taskList:
    #             asyncio.create_task(task)

    # --------------------- DIALOGUE NLP PROCESSING --------------------- ^
    """
        TODO 2,3 ------------------------------------------------------------------------------------------------------------- ^
    """
