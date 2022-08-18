
import pandas as pd
import numpy as np 

class Duplicated_Ids:
    def __init__(self,dataframe,nome_col_id):

        self.dataframe=dataframe.copy()
        self.nome_col_id=nome_col_id
        self.quant_dup_ids=self.dataframe[self.nome_col_id].duplicated().sum()

    def print_duplicated_ids(self,nome_da_tabela):

        print(f'a quantidade de ids duplicados da tabela {nome_da_tabela} são {self.quant_dup_ids}')
    
    def detect_indexes_ids(self):
        #avaliação dos indices duplicados, gerando um dicionario contendo: chave sendo a posição em que o valor foi duplicado, e o valor como sendo uma lista contendo a posição inicial desta chave, e o seu respectivo valor

        if self.quant_dup_ids > 0:
            lista_ids=self.dataframe[self.nome_col_id].tolist()
            dici_ids={}
            temp=[]
            temp_set=set()
            acum,count_val_not_moved=0,0
            val_not_moved=[]

            for k in range(len(lista_ids)):
                temp.append(lista_ids[k])
                temp_set.add(lista_ids[k])

                if len(temp) != len(temp_set):
                   
                    v_arm=lista_ids[k]
                    k_arm=k
                    ini=0
                    fin=-2

                    #iterar pelos extremos, no sentido de identificar o valor de forma mais rápida, caso o array estivesse ordenado, poderia ser utilizado a busca binária, a fim de ser mais rápido ainda
                    #porém, para manter a integridade do array, foi feito desta forma
                    while temp[ini] != v_arm and temp[fin]!=v_arm:
                        ini=ini+1
                
                        fin=-(ini+2)
                    
                    fin=len(temp)+fin

                    
                    val=ini if temp[ini]==v_arm else fin
                    t=temp[:val]
                    
                    count_val_not_moved=val_not_moved.count(v_arm)
                    dici_ids[k_arm]=[val+acum-count_val_not_moved,v_arm]
                    temp=temp[:val]+temp[val+1:]
                    count_val_not_moved=0

                    val_not_moved.extend(t)
                    val_not_moved=list(filter(lambda x: x!=v_arm,val_not_moved))
                    acum+=1

            return dici_ids
           
        else:
            return {}
    
    #agrupamento de valores para retornar como um dicionario contendo os valores e seus indices apresentados no dataframe
    def grouping_indexes(self):

        dict_desordened=self.detect_indexes_ids()
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


        
    #detecação somente dos valores, sem levar em consideração seus indices 
    def detect_values_ids(self):

        if self.quant_dup_ids > 0:
            data_duplicated=self.dataframe[self.nome_col_id].duplicated()
            data_coleted_dup=[self.dataframe[self.nome_col_id][k] for k in range(self.dataframe.shape[0]) if data_duplicated[k]==True]
            return data_coleted_dup
        else:
            return []
   