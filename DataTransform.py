import pandas as pd
import numpy as np 


class DataTransform:
    def __init__(self,dataframe_to_transform):
        self.dataframe_to_transform=dataframe_to_transform
    
    def remove_nans(self,name_columns:list,all=False):
       if all:
        self.dataframe_to_transform.dropna(how='all',inplace=True)
        return self.dataframe_to_transform.reset_index(drop=True)

       self.dataframe_to_transform.dropna(subset=name_columns,inplace=True)
       return self.dataframe_to_transform.reset_index(drop=True)
    
    def remove_dup(self,name_columns:list,all=False):
        if all:
            self.dataframe_to_transform.drop_duplicates(inplace=True)
            return self.dataframe_to_transform.reset_index(drop=True)
        for col in name_columns:
            self.dataframe_to_transform.drop_duplicates(subset=col,inplace=True)
        return self.dataframe_to_transform.reset_index(drop=True)

    def transf_typing(self,name_columns:list,type_expected):
        for col in name_columns:
            tmp=self.dataframe_to_transform.astype({f'{col}':f'{type_expected}'})
            self.dataframe_to_transform=tmp
        return self.dataframe_to_transform