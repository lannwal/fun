
import random
import sys

if(len(sys.argv) > 1):
    args = sys.argv[1]
else:
    args = 'default'

prefix = ['akribische','faktengetriebene','proto',
'numerische','faktengetriebene','quasi','meta','analytische','hochdruck','vacuum','quanten','integriertes','pre','objektifiziert','hermeeutische','hitherto unerforschte','grundlegende','topologische','statistische','technologigetriebene','onotologische', 'demarkante', 'lebenszeit', 'fluktuation', 'stabilitaet', ] 


infix = ['innen','verweildauer','omic','assoziations','guete','modal','zwischenstufen ', 'verteilungs', 'grenzwert', 'statische',]

suffix = ['verschneidung','analyse','studie','kochrezept','ausdauertraining','substrat', 'produkt', 'analysat', 'parser', 'sampler', 'computer', 'test',
 'program','reaktionstank', 'netzwerk', 'cluster', 'labor', 'beweis'] 

print (random.choice(prefix), args ,random.choice(infix), random.choice(suffix))
