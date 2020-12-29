
class evaluations:
    
    def potentialsg(self,muestrapr,listapr):
        cont=0
        longitudtotalmuestrSG=len(muestrapr[:500])
        #print(longitudtotalmuestrSG)
        longitudmuestraSG=0
        for i in range(longitudtotalmuestrSG):
            longitudmuestraSG= len(muestrapr[i])-3
            if longitudmuestraSG == 6:
                if muestrapr[i][3] in listapr[i] or muestrapr[i][4] in listapr[i] or muestrapr[i][5] in listapr[i] or muestrapr[i][6] in listapr[i] or muestrapr[i][7] in listapr[i] or muestrapr[i][8] in listapr[i]:
                    cont+=1        
            if longitudmuestraSG == 5:
                if muestrapr[i][3] in listapr[i] or muestrapr[i][4] in listapr[i] or muestrapr[i][5] in listapr[i] or muestrapr[i][6] in listapr[i] or muestrapr[i][7] in listapr[i]:
                    cont+=1

            if longitudmuestraSG == 4:
                if muestrapr[i][3] in listapr[i] or muestrapr[i][4] in listapr[i] or muestrapr[i][5] in listapr[i] or muestrapr[i][6] in listapr[i]:
                    cont+=1

            if longitudmuestraSG == 3:
                if muestrapr[i][3] in listapr[i] or muestrapr[i][4] in listapr[i] or muestrapr[i][5] in listapr[i]:
                    cont+=1

        print(cont)
        #print(cont/len(muestrapr[:500]))
        
        return (cont/len(muestrapr[:500]))
        
        
    def precisionsg(self,muestrapr,listapr):
        cont=0
        result=list()
        for i in range(len(muestrapr[:500])):
            cont=0
            longitudmuestra=len(muestrapr[i])-3
            longitudlista=len(listapr[i])
            if longitudmuestra == 3:
                if muestrapr[i][3] in listapr[i]:
                    cont+=1
                if muestrapr[i][4] in listapr[i]:
                    cont+=1
                if muestrapr[i][5] in listapr[i]:
                    cont+=1
                result.append(cont/(cont+(longitudlista-cont)))
            if longitudmuestra == 4:
                if muestrapr[i][3] in listapr[i]:
                    cont+=1
                if muestrapr[i][4] in listapr[i]:
                    cont+=1
                if muestrapr[i][5] in listapr[i]:
                    cont+=1
                if muestrapr[i][6] in listapr[i]:
                    cont+=1
                result.append(cont/(cont+(longitudlista-cont)))
            if longitudmuestra == 5:
                if muestrapr[i][3] in listapr[i]:
                    cont+=1
                if muestrapr[i][4] in listapr[i]:
                    cont+=1
                if muestrapr[i][5] in listapr[i]:
                    cont+=1
                if muestrapr[i][6] in listapr[i]:
                    cont+=1
                if muestrapr[i][7] in listapr[i]:
                    cont+=1
                result.append(cont/(cont+(longitudlista-cont)))
            if longitudmuestra == 6:
                if muestrapr[i][3] in listapr[i]:
                    cont+=1
                if muestrapr[i][4] in listapr[i]:
                    cont+=1
                if muestrapr[i][5] in listapr[i]:
                    cont+=1
                if muestrapr[i][6] in listapr[i]:
                    cont+=1
                if muestrapr[i][7] in listapr[i]:
                    cont+=1
                if muestrapr[i][8] in listapr[i]:
                    cont+=1
                result.append(cont/(cont+(longitudlista-cont)))
        suma=0
        #print(len(result))
        for element in result:
            suma+=element
        pr=suma/len(result)
        
        return pr
        
        
    def recallsg(self,muestrarec,listapr):
        cont=0
        resultrec=list()
        longitudmuestra=0
        longitudlista=0
        for i in range(len(muestrarec[:500])):
            cont=0
            longitudmuestra=len(muestrarec[i])-3
            longitudlista=len(listapr[i])
            if longitudmuestra == 3:
                if muestrarec[i][3] in listapr[i]:
                    cont+=1
                if muestrarec[i][4] in listapr[i]:
                    cont+=1
                if muestrarec[i][5] in listapr[i]:
                    cont+=1
                #resultrec.append((cont*100)/longitudmuestra)
                resultrec.append(cont/(cont+(longitudmuestra-cont)))
            if longitudmuestra == 4:
                if muestrarec[i][3] in listapr[i]:
                    cont+=1
                if muestrarec[i][4] in listapr[i]:
                    cont+=1
                if muestrarec[i][5] in listapr[i]:
                    cont+=1
                if muestrarec[i][6] in listapr[i]:
                    cont+=1
                #resultrec.append((cont*100)/longitudmuestra)
                resultrec.append(cont/(cont+(longitudmuestra-cont)))
            if longitudmuestra == 5:
                if muestrarec[i][3] in listapr[i]:
                    cont+=1
                if muestrarec[i][4] in listapr[i]:
                    cont+=1
                if muestrarec[i][5] in listapr[i]:
                    cont+=1
                if muestrarec[i][6] in listapr[i]:
                    cont+=1
                if muestrarec[i][7] in listapr[i]:
                    cont+=1
                #resultrec.append((cont*100)/longitudmuestra)
                resultrec.append(cont/(cont+(longitudmuestra-cont)))
            if longitudmuestra == 6:
                if muestrarec[i][3] in listapr[i]:
                    cont+=1
                if muestrarec[i][4] in listapr[i]:
                    cont+=1
                if muestrarec[i][5] in listapr[i]:
                    cont+=1
                if muestrarec[i][6] in listapr[i]:
                    cont+=1
                if muestrarec[i][7] in listapr[i]:
                    cont+=1
                if muestrarec[i][8] in listapr[i]:
                    cont+=1
                #resultrec.append((cont*100)/longitudmuestra)
                resultrec.append(cont/(cont+(longitudmuestra-cont)))
        sumarec=0
        for element in resultrec:
            sumarec+=element
        rec=sumarec/len(resultrec)
        return rec
        
    def f1sg(self,pr,rec):
        f1=0
        f1=2*((pr*rec)/(pr+rec))
        return f1
        
    def potentialss(self,muestraSS,result):
        cont=0
        longitudtotalmuestrSS=len(muestraSS[:500])
        print(longitudtotalmuestrSS)
        longitudmuestraSS=0
        for i in range(longitudtotalmuestrSS):
            longitudmuestraSS= len(muestraSS[i])-5
            if longitudmuestraSS == 6:
                if muestraSS[i][5] in result[i] or muestraSS[i][6] in result[i] or muestraSS[i][7] in result[i] or muestraSS[i][8] in result[i] or muestraSS[i][9] in result[i] or muestraSS[i][10] in result[i]:
                    cont+=1        
            if longitudmuestraSS == 5:
                if muestraSS[i][5] in result[i] or muestraSS[i][6] in result[i] or muestraSS[i][7] in result[i] or muestraSS[i][8] in result[i] or muestraSS[i][9] in result[i]:
                    cont+=1

            if longitudmuestraSS == 4:
                if muestraSS[i][5] in result[i] or muestraSS[i][6] in result[i] or muestraSS[i][7] in result[i] or muestraSS[i][8] in result[i]:
                    cont+=1

            if longitudmuestraSS == 3:
                if muestraSS[i][5] in result[i] or muestraSS[i][6] in result[i] or muestraSS[i][7] in result[i]:
                    cont+=1

        #print(cont)
        #print(cont/longitudtotalmuestrSS)
        return(cont/longitudtotalmuestrSS)
        
        
    def precisionss(self,muestraSS,result):
        cont=0
        resultpre=list()
        for i in range(len(muestraSS[:500])):
            cont=0
            longitudmuestra=len(muestraSS[i])-5
            longitudlista=len(result[i])
            if longitudmuestra == 3:
                if muestraSS[i][5] in result[i]:
                    cont+=1
                if muestraSS[i][6] in result[i]:
                    cont+=1
                if muestraSS[i][7] in result[i]:
                    cont+=1
                resultpre.append(cont/(cont+(longitudlista-cont)))
            if longitudmuestra == 4:
                if muestraSS[i][5] in result[i]:
                    cont+=1
                if muestraSS[i][6] in result[i]:
                    cont+=1
                if muestraSS[i][7] in result[i]:
                    cont+=1
                if muestraSS[i][8] in result[i]:
                    cont+=1
                resultpre.append(cont/(cont+(longitudlista-cont)))
            if longitudmuestra == 5:
                if muestraSS[i][5] in result[i]:
                    cont+=1
                if muestraSS[i][6] in result[i]:
                    cont+=1
                if muestraSS[i][7] in result[i]:
                    cont+=1
                if muestraSS[i][8] in result[i]:
                    cont+=1
                if muestraSS[i][9] in result[i]:
                    cont+=1
                resultpre.append(cont/(cont+(longitudlista-cont)))
            if longitudmuestra == 6:
                if muestraSS[i][5] in result[i]:
                    cont+=1
                if muestraSS[i][6] in result[i]:
                    cont+=1
                if muestraSS[i][7] in result[i]:
                    cont+=1
                if muestraSS[i][8] in result[i]:
                    cont+=1
                if muestraSS[i][9] in result[i]:
                    cont+=1
                if muestraSS[i][10] in result[i]:
                    cont+=1
                resultpre.append(cont/(cont+(longitudlista-cont)))
        sumaprSS=0
        for element in resultpre:
            sumaprSS+=element
        precss=sumaprSS/len(resultpre)
        return precss
        
    def recallss(self,muestraSS,result):
        cont=0
        resultrec=list()
        for i in range(len(muestraSS[:500])):
            cont=0
            longitudmuestra=len(muestraSS[i])-5
            longitudlista=len(result[i])
            if longitudmuestra == 3:
                if muestraSS[i][5] in result[i]:
                    cont+=1
                if muestraSS[i][6] in result[i]:
                    cont+=1
                if muestraSS[i][7] in result[i]:
                    cont+=1
                #resultrec.append((cont*100)/longitudmuestra)
                resultrec.append(cont/(cont+(longitudmuestra-cont)))
            if longitudmuestra == 4:
                if muestraSS[i][5] in result[i]:
                    cont+=1
                if muestraSS[i][6] in result[i]:
                    cont+=1
                if muestraSS[i][7] in result[i]:
                    cont+=1
                if muestraSS[i][8] in result[i]:
                    cont+=1
                #resultrec.append((cont*100)/longitudmuestra)
                resultrec.append(cont/(cont+(longitudmuestra-cont)))
            if longitudmuestra == 5:
                if muestraSS[i][5] in result[i]:
                    cont+=1
                if muestraSS[i][6] in result[i]:
                    cont+=1
                if muestraSS[i][7] in result[i]:
                    cont+=1
                if muestraSS[i][8] in result[i]:
                    cont+=1
                if muestraSS[i][9] in result[i]:
                    cont+=1
                #resultrec.append((cont*100)/longitudmuestra)
                resultrec.append(cont/(cont+(longitudmuestra-cont)))
            if longitudmuestra == 6:
                if muestraSS[i][5] in result[i]:
                    cont+=1
                if muestraSS[i][6] in result[i]:
                    cont+=1
                if muestraSS[i][7] in result[i]:
                    cont+=1
                if muestraSS[i][8] in result[i]:
                    cont+=1
                if muestraSS[i][9] in result[i]:
                    cont+=1
                if muestraSS[i][10] in result[i]:
                    cont+=1
                #resultrec.append((cont*100)/longitudmuestra)
                resultrec.append(cont/(cont+(longitudmuestra-cont)))
        sumarecSS=0
        for element in resultrec:
            sumarecSS+=element
        recss=sumarecSS/len(resultrec)
        return recss
        
    def f1ss(self,pr,rec):
        f1ss=0
        f1ss=2*((pr*rec)/(pr+rec))
        return f1ss