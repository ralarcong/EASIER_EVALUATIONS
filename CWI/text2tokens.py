import os
import spacy
import re
class text2tokens:
    nlp = spacy.load('es_core_news_md')
    
    def text2sentencestokens(self, text):
        listapalabras=list()
        document = self.nlp(text)

        for i,s in enumerate(document.sents):
            #print("*********Oracion**************",i)
            chunks=self.getchunks(s.text)
            length=len(chunks)
            for x in range(length): 
                listapalabras.append((["P" + str(x), s, (s.text).index(chunks[x]), (s.text).index(chunks[x])+len(chunks[x]), chunks[x], 10, 10, 0, 1,1, 0.05]))
            for j,token in enumerate(s):
                #print("original:", token.orth_)
                #print("PoS tag:", token.pos_)
                #print(token.idx,token.idx+len(token.orth_))
                if (token.pos_=='ADJ' or token.pos_=='ADV' or token.pos_=='NOUN' or token.pos_=='VERB' or token.pos_=='PROPN'):
                    listapalabras.append((["P" + str(i), (s.text), token.idx, token.idx+len(token.orth_), token.orth_, 10, 10, 0, 1,1, 0.05]))
                
        return listapalabras
  
    def getchunks(self,s):
        listachunks=list()
        oracion=self.nlp(s)
        for chunk in oracion.noun_chunks:
            if(len((chunk.text).split())>1):
                listachunks.append(chunk.text)
        return listachunks
    
    
    def text2sentences(self,text):
        listaoraciones=list()
        document = self.nlp(text)
        for i,s in enumerate(document.sents):
            listaoraciones.append(s.text)
        
        return listaoraciones
    
    def sentence2tokens(self,sentence):
        listapalabras=list()
        oracion=self.nlp(sentence)
        chunks=self.getchunks(oracion.text)
        length=len(chunks)
        for x in range(length): 
            listapalabras.append((["P" + str(x), oracion.text, (oracion.text).index(chunks[x]), sentence.index(chunks[x])+len(chunks[x]), chunks[x], 10, 10, 0, 1,1, 0.05]))
        for j,token in enumerate(oracion):
            #print("original:", token.orth_)
            #print("PoS tag:", token.pos_)
            #print(token.idx,token.idx+len(token.orth_))
            if (token.pos_=='ADJ' or token.pos_=='ADV' or token.pos_=='NOUN' or token.pos_=='VERB' or token.pos_=='PROPN'):
                listapalabras.append((["P" + str(j), (oracion.text), token.idx, token.idx+len(token.orth_), token.orth_, 10, 10, 0, 1,1, 0.05]))      
        return listapalabras
    

    def ContainPunctuation(self,word):
        regexp = re.compile(r'[\•\“\”\°]+')
        if regexp.search(word):
            return 1
        else:
            return 0
    
    
    
    
    
    
    
    
    
    def text2sentences2(self,text,ini):
        listaoraciones=list()
        document = self.nlp(text)
        cont=0
        for i,s in enumerate(document.sents):
            cont=cont+1 
        if cont==1:
            for i,s in enumerate(document.sents):
                listaoraciones.append([s.text,ini])
            return listaoraciones,ini+len(s.text)
        else:
            temp=ini
            for i,s in enumerate(document.sents):
                listaoraciones.append([s.text,temp])
                temp=temp+len(s.text)
            return listaoraciones,temp

        
    
    def sentence2tokens2(self,sentence,ini):
        listapalabras=list()
        oracion=self.nlp(sentence)
        #chunks=self.getchunks(oracion.text)
        #length=len(chunks)
        #for x in range(length): 
         #   listapalabras.append((["P" + str(x), oracion.text, (oracion.text).index(chunks[x]), sentence.index(chunks[x])+len(chunks[x]), chunks[x], (oracion.text).index(chunks[x])+ini, sentence.index(chunks[x])+len(chunks[x])+ini, 0, 1,1, 0.05]))
        for j,token in enumerate(oracion):
            #print("original:", token.orth_)
            #print("PoS tag:", token.pos_)
            #print(token.idx,token.idx+len(token.orth_))
            if(self.ContainPunctuation(token.text)==0):
                if (token.pos_=='ADJ' or token.pos_=='ADV' or token.pos_=='NOUN' or token.pos_=='VERB' or token.pos_=='PROPN'):
                    listapalabras.append((["P" + str(j), (oracion.text), token.idx, token.idx+len(token.orth_), token.orth_, token.idx+ini, token.idx+len(token.orth_)+ini, token.pos_, 1,1, 0.05]))      
        return listapalabras

    
  
    


    def __init__(self):
            self.data = []
