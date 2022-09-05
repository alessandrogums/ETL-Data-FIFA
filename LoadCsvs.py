import os

class LoadCsvs:
    def __init__(self,dataframe):
        self.dataframe=dataframe
    
    def load_csv(self,name_dataframe,new_folder):
        path=f'../ETL-Data-FIFA/{new_folder}'
        if not os.path.exists(path=path):
            os.makedirs(path)
        
        return self.dataframe.to_csv(f'{new_folder}/{name_dataframe}.csv')
            