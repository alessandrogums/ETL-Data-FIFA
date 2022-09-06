
import pandas as pd
import numpy as np 

class AnalyzeDuplicatedData:
    def __init__(self,dataframe,name_col_data):

        self.dataframe=dataframe.copy()
        self.name_col_data=name_col_data
        self.quant_dup_data=self.dataframe[self.name_col_data].duplicated().sum()

    def print_duplicated_data(self,table_name):

        print(f'a quantidade de dados duplicados da tabela {table_name}  na coluna {self.name_col_data} são {self.quant_dup_data}')
    
    def detect_indexes_data(self):
        #avaliação dos indices duplicados, gerando um dicionario contendo: chave sendo a posição em que o valor foi duplicado, e o valor como sendo uma lista contendo a posição inicial desta chave, e o seu respectivo valor

        if self.quant_dup_data > 0:
            list_data=self.dataframe[self.name_col_data].tolist()
            dici_data={}
            temp=[]
            temp_set=set()
            acum,count_val_not_moved=0,0
            val_not_moved=np.array([])

            for k in range(len(list_data)):
                temp.append(list_data[k])
                temp_set.add(list_data[k])
              
                if len(temp) != len(temp_set):
                   
                    v_arm=list_data[k]
                    k_arm=k
                    ini=0
                    fin=-2

                    #iterar pelos extremos, no sentido de identificar o valor de forma mais rápida, caso o array estivesse ordenado, poderia ser utilizado a busca binária, a fim de ser mais rápido ainda
                    #porém, para manter as posições reais equivalantes no Df, foi feito dessa forma 
                    # while temp[ini] != v_arm and temp[fin]!=v_arm:
                    #     ini=ini+1
                
                    #     fin=-(ini+2)
                    
                    # fin=len(temp)+fin
                    # val=ini if temp[ini]==v_arm else fin
                    for ini in range(len(temp)//2 + 1):
                        fin=-(ini+2)
                        if temp[ini] ==v_arm:
                            val=ini
                            break
                        elif temp[fin]==v_arm:
                            val=len(temp)+fin
                            break
                   
                 
                    t=np.array(temp[:val])
                
                    count_val_not_moved=np.count_nonzero(val_not_moved == v_arm)

                    dici_data[k_arm]=[val+acum-count_val_not_moved,v_arm]
                    temp=temp[:val]+temp[val+1:]
                    count_val_not_moved=0
                    val_not_moved=np.concatenate((val_not_moved,t),axis=0)
                    val_not_moved=np.setdiff1d(val_not_moved,[v_arm])
                   
                    acum+=1

            return dici_data
        else:
            return {}
    
    
    #agrupamento de valores para retornar como um dicionario contendo os valores e seus indices apresentados no dataframe
    def grouping_indexes(self):
        if self.quant_dup_data > 0:
            dict_desordened=self.detect_indexes_data()
            ord=dict(sorted(dict_desordened.items(), key=lambda y: y[1][1]))
            new_dici={}
            acum=((list(ord.keys())[0]))

            for value in ord.values():
                
                if acum==value[1]:
                    tmp=new_dici[acum]
                    tmp.append(value[0])
                    new_dici[acum]=tmp
                else:
                    new_dici[value[1]]=[value[0]]
                    acum=value[1]
            return new_dici 
        else:
            return None


        
    #detecação somente dos valores, sem levar em consideração seus indices 
    def detect_values_data(self):

        if self.quant_dup_data > 0:
            data_duplicated=self.dataframe[self.name_col_data].duplicated()
            data_coleted_dup=[self.dataframe[self.name_col_data][k] for k in range(self.dataframe.shape[0]) if data_duplicated[k]==True]
            return data_coleted_dup
        else:
            return []
   