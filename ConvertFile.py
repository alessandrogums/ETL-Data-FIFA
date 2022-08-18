import pandas as pd
import os 


class Convert_File_to_pd:
    def __init__(self,file_name:str,name_table:str,folder_name:str) -> None:
        self.file_name=file_name
        self.name_table=name_table
        self.folder_name=folder_name

    

    @staticmethod
    def transform(string):
        special_chars='-_+*()\./= '
        for char in special_chars:
            string=string.replace(char,'')
        return string.lower()
    
   
    @property
    def search_file(self):
        file_arch=self.transform(self.file_name)
        ls=os.listdir()
        ls=os.listdir(f'../{self.folder_name}/{self.name_table}/')
        dici={p:ls[p] for p in range(len(ls))}
        
        for key,value in dici.items():
            value_transf=self.transform(value)
        
            if value_transf[:-3]  == file_arch or value_transf[:-4] ==file_arch:
                
                    return (dici[key],dici[key][-(dici[key][::-1].index('.')):])
            
        raise  FileNotFoundError 
    

    @property
    def convert_to_dataframe(self):
        
        if self.search_file[1] =='csv':
            return pd.read_csv(f'../{self.folder_name}/{self.name_table}/{self.search_file[0]}')

        elif self.search_file[1]=='xls':
            return pd.read_excel(f'../{self.folder_name}/{self.name_table}/{self.search_file[0]}')

        elif self.search_file[1]=='xlsx':
            return pd.read_excel(f'../{self.folder_name}/{self.name_table}/{self.search_file[0]}', engine='openpyxl')
            
        elif self.search_file[1]=='json':
            return pd.read_json(f'../{self.folder_name}/{self.name_table}/{self.search_file[0]}')