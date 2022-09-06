import pandas as pd
import numpy as np 


class DataTransform:
    def __init__(self,dataframe_to_transform):
        self.dataframe_to_transform=dataframe_to_transform
    
    def remove_nans(self,name_column:list,all=False):
       if all:
        self.dataframe_to_transform.dropna(how='all',inplace=True)
        return self.dataframe_to_transform.reset_index()

       self.dataframe_to_transform.dropna(subset=name_column,inplace=True)
       return self.dataframe_to_transform.reset_index()
    
    def remove_dup(self,name_column:list,all=False):
        if all:
            self.dataframe_to_transform.drop_duplicates(inplace=True)
            return self.dataframe_to_transform
        for col in name_column:
            self.dataframe_to_transform.drop_duplicates(subset=col,inplace=True)
        return self.dataframe_to_transform.reset_index()

    def transf_typing(self,name_column:str,type_expected):
        return self.dataframe_to_transform.astype({f'{name_column}':f'{type_expected}'})
