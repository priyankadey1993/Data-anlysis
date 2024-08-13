# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:14:59 2024

@author: soura
"""

'''
1.	Create a string “Grow Gratitude”.
Code for the following tasks:
a)	How do you access the letter “G” of “Growth”?
b)	How do you find the length of the string?
c)	Count how many times “G” is in the string?

'''

str1 ='Grow Gratitude'
#	How do you access the letter “G” of “Growth”?
print(str1[0])
print("length of the string",len(str1))
print("count of g in str1",str1.count("G"))


#-------------------------------------------------------------------------------------------------------------------------------------#
'''
2.	Create a string “Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.”
Code for the following:
a)	Count the number of characters in the string.

'''
str2= "Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else."
import re 
m = re.findall(r"[\w]", str2)
print("total count of wosentance word",len(m))


#-------------------------------------------------------------------------------------------------------------------------------------#
'''
3.	Create a string "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
Code for the following tasks:
a)	get one char of the word
b)	get the first three char

'''
str3="Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
#get one char of the word
charindex=6
print("one character of the word is ",str3[6])
print("1st three character of the swntance ",str3[0:3])
print("last 3 character of the santace  ",str3[-3:])


#-------------------------------------------------------------------------------------------------------------------------------------#
'''
create a string "stay positive and
optimistic". Now write a code to split on whitespace.
Write a code to find if:
a)      The string starts with “H”
b)     The string ends with “d”
c)      The string ends with “c”

'''

text="stay positive and optimistic" 

words = text.split()
print(words)

start_with_h= text.startswith("H")
print("test start with h",start_with_h)

start_with_d= text.endswith("D")
print("test end with d",start_with_d)

start_with_c= text.endswith("C")
print("test end with c",start_with_c)


#-------------------------------------------------------------------------------------------------------------------------------------#
'''
5.	Write a code to print " 🪐 " one hundred and eight times.
'''
for i in range (108):
    print("🪐")


#-------------------------------------------------------------------------------------------------------------------------------------#
'''
6.	Create a string “Grow Gratitude” and write a code to replace “Grow” with “Growth of”

'''
str6= 'Grow Gratitude'
new_word='Growth of'
if ("Grow"  in str6):
    str6.replace("Grow", "Growth of")
    str6
else:
    print("not preset")


#-------------------------------------------------------------------------------------------------------------------------------------#
'''
7.	A story was printed in a pdf, which isn’t making any sense. i.e.:
“.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdeci
tondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .
mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yad
emosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpu
ekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A”

You have noticed that the story is printed in a reversed order. Rectify the same and write a code to print the same story in the correct order.

'''

str7=".elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A"

print(str7[::-1])