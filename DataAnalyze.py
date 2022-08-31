
import pandas as pd 
import numpy as np
import re 
from cmath import isnan

class DataAnalyze:

    def __init__(self,dataframe):
        self.dataframe=dataframe
    



    def count_nans(self,name_columns:list):
        dici_data={}
        for col in name_columns:
            ls=self.dataframe[col].tolist()
            c_nan=[True for c in ls if  isinstance(c,float) and isnan(c)==True]
            
            if c_nan==[]:
                dici_data[col]=0
            else:
                prop_nan=(sum(c_nan)/len(ls))*100
                dici_data[col]=prop_nan
        return dici_data



    def detect_nans(self,name_column):
        data_nans=self.dataframe[name_column].isna()
        if True in data_nans:
            indexes_nans= [i for i in range(self.dataframe.shape[0]) if data_nans[i]==True]
            return f'lista  indices contendo nans: {indexes_nans}'
        else:
            return 'não contém nans nesta coluna'
    


    def identify_outliers_IQR(self,name_column):
        array_col=np.array(self.dataframe[name_column])
        q1,q3=np.percentile(array_col,[25,75])
        iqr=q3-q1
        lower_rang=q1-(1.5*iqr)
        upp_rang=q3+(1.5*iqr)
        
        vet_out=[v for v in array_col if v<lower_rang or v>upp_rang]
        return vet_out



    def identify_outliers_z_score_mod(self,name_column):
        #o método Z-Score relaciona se baseia na investigação de um certo dado em como ele se relaciona com a média e o desvio padrão do grupo com o qual este dado está inserido
        # A fórmula é representada da seguinte forma: z = (x – μ)/σ
        #onde o x é a amostra avaliada, mi a média e o sigma o desvio padrão
        # Para identificação do outlier, este valor não pode passar de 3 ou -3
        #para tratar os dados antes de passar pelo loop, quando passar por um NaN

        #O método Z-score trata bem outliers quando a amostra afeta sigficativamente na distribuição gaussiana e quando a amostra possui um conjunto de dados grande
        #No entanto, quando esses dois parâmetros são contrários, o desvio padrao e média acabam sendo bastante afetados pelos outliers
        #Sendo assim, existe uma fórmula modificada para tornar o z-score ainda mais robusto para os seus pontos limitantes

        #fórmula=0.6745(valor_amostra - mediana)/desvio absoluto mediano(Mad)

        #A mediana e MAD são medidas robustas de tendência central e dispersão, de forma respectiva



        #Autores :Giampaolo E. D'Errico and Nadir Murru , artigo "Fuzzy Treatment of Candidate Outliers in Measurements"

        try:
            #para tratar os dados antes de passar pelo loop, quando passar por um NaN
            data_filter=self.dataframe[name_column].replace({np.nan:0})

            #transformando os dados para float, para agregar tanto os núms flutantes, como os ints
            transform_float=list(map(lambda x:float(x),data_filter))
            median=np.median(np.array(transform_float))
            Mad=np.median([(abs(y-median)) for y in transform_float])
            const=0.6745
            validador=3.5 
            outliers={}

        #os valores serão armazenados em um dicionário representando o indice:[valor do mi, valor sob este indice]"
            
            for lin in range(self.dataframe.shape[0]):
                value=transform_float[lin]
                mi=const*(value-median)/Mad

                if mi > validador or mi <-validador:
                    outliers[lin]=[mi,value]
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
        else:
            return 'all the data are in the date structure'

    @staticmethod
    def convert_string_to_number(string,type_ness,type_def):
        try:
            ini= type_ness(eval(str(string)))
            to=type_def(eval(str(string)))
            if ini==to: return True
        except:
            return None
