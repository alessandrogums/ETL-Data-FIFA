#Primeiramente, para detectarmos onde podemos slicear as tags, é necessário avaliar os padrões não só entre os registros dentro da coluna, como também entre elas 
#Para isso, essas classe abaixo irá ser responsável por isso

class ObsMatchFields:
      
   
      def __init__(self,Df) -> None:
        self.Df=Df
        
    
    #Sendo a cleaning_tags irá limpar dados, exceto </ e < para podermos identificar aonde termina e aonde começa a tag
      def cleaning_tags(self,name_column):
         for  key,value in enumerate(self.Df[name_column]):
            strin=""
            for i in range(len(value)):

                if value[i] =='<' or value[i] == '/':
                    strin+=value[i]
                elif value[i] =='>':
                    strin+=" "
                elif value[i].isalpha()==True:
                    strin+=value[i]
            

            d=strin.split(" ")
        
            self.Df[name_column][key]=d
     


     #Já detect_patt detecta o nome padrão e o intervalo aonde aparece a tag começando com < e aonde ela termina(</)
     #Ainda mais, ela avalia o padrão entre as linhas dessa determinada coluna 
      def detect_patt(self,name_column):
        
        treatment=self.cleaning_tags(name_column)
        dici={}
        for i,j in self.Df[name_column].iteritems():
            marc=0
            for s in range(len(j)-1):
              
                var=self.Df[name_column][i][marc]
                if var[0]=="<" :
                    tmp="</"+var[1:]
                    ls=j[marc+1:]
                    if  tmp in ls:
                        pos=ls.index(tmp)
                        if var in dici.keys():
                            r=dici[var]
                            r.append(pos)
                            dici[var]=r
                        else:
                            dici[var]=[pos]
                    
                marc+=1
                # else:
                #     break



            # if dici_tot=={}:
            #     dici_tot=dici
            # else:
            #     temp1=set(dici.keys())
            #     temp2=set(dici_tot.keys())
                
            #     inters=temp2.intersection(temp1)
            #     dici_t={item:dici_tot[item]+dici[item] for item in inters}
            #     dici_tot=dici_t.copy()
        

        dici_upd={k:(sum(v)//self.Df.shape[0]) for k,v in dici.items()}
        return dici_upd

    
      #essa última função irá gerar os padrões  entre as colunas comuns a elas
      #Identificando o valor máximo, ou seja, o máximo irá englobar as demais e ocorrerá a repetição
      def valid_gen(self):
        dici_fin={}
        name_cols=self.Df.columns.tolist()
        for n in name_cols:
            dicis_cols=self.detect_patt(n)
            if dici_fin=={}:
                dici_fin=dicis_cols
            else:
                temp1=set(dicis_cols.keys())
                temp2=set(dici_fin.keys())

                inters_fin=temp2.intersection(temp1)
                dici_temp={item:dici_fin[item]+dicis_cols[item] for item in inters_fin}
                dici_fin=dici_temp


    
        dici_max={k:v//len(name_cols) for k,v in dici_fin.items()}
        f=sorted(dici_max.items(),key=lambda x: x[1],reverse=True)[0]
        return f