#!/usr/bin/env python
# encoding=utf8
import pyphen


class Pyphen:
    dic=pyphen.Pyphen(lang='es')
    
    def getNSyl(self,word):
        #if len(word.split())<2:
        try:
            test = self.dic.inserted(word)
            count=0
            for i in test:
                if i == '-':
                    count = count + 1
            count += 1
            return count
        except:
            test = self.dic.inserted(str(word))
            #print(test)
            count=0
            for i in test:
                if i == '-':
                    count = count + 1
            count += 1
            return count
#        else:
#            tokens=word.split()
#            lastword=0
#            try:
#                for palabra in tokens:
#                    test = self.dic.inserted(palabra)
#                    print(palabra)
#                    count=0
#                    for i in test:
#                        if i == '-':
#                            count = count + 1
#                    count += 1
#                    if count>lastword:
#                        lastword=count
#                    else:
#                        lastword=count     
#                return count
#            except:
#                for palabra in tokens:
#                    test = self.dic.inserted(str(palabra))
#                    print(palabra)
 #                   count=0
#                    for i in test:
#                        if i == '-':
#                            count = count + 1
#                    count += 1
 #                   if count>lastword:
 #                       lastword=count
 #                   else:
 #                       lastword=count     
#                return count
                
            

