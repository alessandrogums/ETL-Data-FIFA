import json
#classe encarregada de desserializar os campos json, transformando em chave-valor vide dicionário em py
#Após isso, carregar os dados em novas colunas no dataframe, deletando essa coluna cuja estrutura é JSON

class JsonLoadsCols:
        def __init__(self,dataframe,name_Col:str):
            self.dataframe=dataframe
            self.name_col=name_Col
        
        def desserialize_data(self):
            dici_new_cols={}
            for k in self.dataframe[self.name_col]:
                x=json.loads(k)
                for i in x.keys():
                    if i not in  dici_new_cols.keys():
                        dici_new_cols[i]=[x[i]]
                    else:
                        dici_new_cols[i].append(x[i])
            return dici_new_cols
        
        def load_data(self):
            dici_loads=self.desserialize_data()
            for x in dici_loads.keys():
                self.dataframe[x]=dici_loads[x]
            
            self.dataframe.drop([self.name_col],axis=1,inplace=True)
            self.dataframe.drop(['Unnamed: 0'],axis=1,inplace=True)
            return self.dataframe
