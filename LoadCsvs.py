import os

#classe responsável por carregar os csvs dos dfs gerados

class LoadCsvs:
    def __init__(self,dataframe,new_folder,name_dataframe,folder_name):
        self.dataframe=dataframe
        self.new_folder=new_folder
        self.name_dataframe=name_dataframe
        self.folder_name=folder_name

    @property
    def load_csv(self):
        path=f'../{self.folder_name}/{self.new_folder}'
        if not os.path.exists(path=path):
            os.makedirs(path)
        
        return self.dataframe.to_csv(f'{self.new_folder}/{self.name_dataframe}.csv')
            