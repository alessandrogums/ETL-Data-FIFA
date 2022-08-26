
import pandas as pd 
import numpy as np
import re 

class DataAnalyze:

    def __init__(self,dataframe):
        self.dataframe=dataframe
    

    def detect_nans(self,name_column):
        data_nans=self.dataframe[name_column].isna()
        if True in data_nans:
            indexes_nans= [i for i in range(self.dataframe.shape[0]) if data_nans[i]==True]
            return f'lista  indices contendo nans: {indexes_nans}'
        else:
            return 'não contém nans nesta coluna'
    

    def identify_outliers(self,name_column):
        #o método Z-Score relaciona se baseia na investigação de um certo dado em como ele se relaciona com a média e o desvio padrão do grupo com o qual este dado está inserido
        # A fórmula é representada da seguinte forma: z = (x – μ)/σ
        #onde o x é a amostra avaliada, mi a média e o sigma o desvio padrão
        # Para identificação do outlier, este valor não pode passar de 3 ou -3
        #para tratar os dados antes de passar pelo loop, quando passar por um NaN

        try:
            #para tratar os dados antes de passar pelo loop, quando passar por um NaN
            data_filter=self.dataframe[name_column].replace({np.nan:0})

            #transformando os dados para float, para agregar tanto os núms flutantes, como os ints
            transform_float=list(map(lambda x:float(x),data_filter))
            media=sum(transform_float)/len(data_filter)
            desv_pad=np.std(transform_float)  
            validador=3
            outliers={}

        #os valores serão armazenados em um dicionário representando o indice:[valor do z, valor sob este indice]"
            
            for lin in range(self.dataframe.shape[0]):
                value=transform_float[lin]
                z=(value - media)/desv_pad
                if z > validador or z<-validador:
                    outliers[lin]=[z,value]
            return outliers 

        except ValueError:
            print("O dado não pode ser convertido pra float")
    

    def confirm_typing(self,name_column,type_expected):
        types={'float':1.11,'integer':2,'int':33,'str':'string','dict':{1:3},list:[]}
        if types.get(type_expected) != None:
            type_exp=types[type_expected]
            conf=[t for t in self.dataframe[name_column] if type(t)!=type(type_exp)]    
            return conf 
        else:
            return 'escreva a tipagem correta'

    def analyze_typing_expected_number(self,expected_type_number,name_column):
        #geração de um dicionário contendo os dados que podem corresponder a uma variável numérica 


        patt={'float':1.11,'integer':2,'int':33}
      
        if patt.get(expected_type_number)!=None:
            dici_val={}
            type_expect=patt[expected_type_number]
            for key,_ in self.dataframe.iterrows():
                    act_val=self.dataframe[name_column][key]
                    if isinstance(act_val,str) and  isinstance(type_expect,int):

                        rgx_int="^((0?[1-9]{0,1})|^[1-9]{1}[0-9]*)([.]{1}[0]{1})?$"
                        ident=re.match(rgx_int,act_val.replace(",",".").strip())
                        if ident == None:
                            dici_val[key]=[act_val,'detected str, expected structure type int']
                    
                    elif isinstance(act_val,str) and  isinstance(type_expect,float):

                        rgx_float="(^([1-9]{1}[0-9]*)([.][0-9]+)?$)|^([0]{1})([.][0-9]+)?$"
                        ident=re.match(rgx_float,act_val.replace(",",".").strip())
                        if ident == None:
                            dici_val[key]=[act_val,'detect str, expected structure type float']

                    elif isinstance(act_val,float) and isinstance(type_expect,int):

                        compare=self.convert_string_to_number(act_val,float,int)
                        if compare != None:
                            dici_val[key]=[act_val,'same expected value between int and float typing']

                    elif isinstance(act_val,bool):

                        dici_val[key]=[act_val,f'detect bool, expected your integer ->{int(act_val)}']
                        
            return dici_val
                    
        else:
            return 'escreva a tipagem correta'
    

    def analyze_typing_expected_timestamp(self,name_column):
        data_test=self.dataframe.copy()
        data_test[name_column]=pd.to_datetime(self.dataframe[name_column], errors='coerce')
        number_of_na=data_test.index[data_test[name_column].isna()].tolist()
        if len(number_of_na) != 0:
            list_values=[self.dataframe.loc[v,name_column] for v in number_of_na]

        return list_values


    @staticmethod
    def convert_string_to_number(string,type_ness,type_def):
        try:
            ini= type_ness(eval(str(string)))
            to=type_def(eval(str(string)))
            if ini==to: return True
        except:
            return None
