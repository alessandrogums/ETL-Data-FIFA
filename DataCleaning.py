import pandas as pd
import numpy as np 


class DataCleaning:
    def __init__(self,dataframe_to_cleaned) -> None:
        self.dataframe_to_cleaned=dataframe_to_cleaned
    
    def remove_nans(self,name_column:list,all=True):
       if all:
        data_cleaned=self.dataframe_to_cleaned.dropna(how='all').reset_index(drop=True)
       data_cleaned=self.dataframe_to_cleaned.dropna(subset=name_column).reset_index(drop=True)

       return data_cleaned
    
    def remove_dup(self,name_column:list,all=True):
        if all:
            data_cleaned=self.dataframe_to_cleaned.drop_duplicates().reset_index(drop=True)
        data_cleaned=self.dataframe_to_cleaned.drop_duplicates(subset=name_column).reset_index(drop=True)
        return data_cleaned