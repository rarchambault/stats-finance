                                                        #exercise 1
# def to_miles(km):
#     km = km*0.6214
#     return km 

# mesure = float(input("Enter a mesure: "))
# calcul = round(to_miles(mesure),2)
# print(str(mesure) +" km equals " + str(calcul) + " miles.")

                                                        #exercise 2
# import string


# def toTime(i):
    
#     seconds = i % 60
#     left_min_heure_ensec = i - seconds
#     left_min_heure_enmin = left_min_heure_ensec/60
#     minutes = left_min_heure_enmin % 60
#     left_heure_enmin = left_min_heure_enmin - minutes
#     heures = left_heure_enmin/60
#     string = str(heures) + " hours :: " + str(minutes) + " minutes :: " + str(seconds) + " seconds"
#     return string

# time = int(input("Enter a time in seconds: "))
# conversion = toTime(time)
# print(conversion)

                                                        #exercise 3

# def numbers_stats():
#     x=[] 
#     for i in range(int(input("How many elements are in list : "))): 
#         x.append(int(input("Enter number "+ str(i+1)+": ")))
#     cumu = 0
#     for o in range(len(x)):
#         cumu += x[o] 
#     average = cumu / len(x)
#     x.sort()
#     max = x[(len(x)-1)]
#     min = x[0]
#     print(" The largest number is " + str(max) + ", the smallest one is " + str(min) +  " and the average is " + str(average))
# numbers_stats()

# a  refaire en faisant des for pour le max et min et input le array

from operator import index


def chienne(grosse_plote):
    RammasisDeMarde = 0
    tit_penis = 0    
    gros_penis = 0
    tabarnak = 0
    for tapette in range(len(grosse_plote)):
        if grosse_plote[tapette] < tit_penis or tapette == 0:
            tit_penis = grosse_plote[tapette]
        if grosse_plote[tapette] > gros_penis:
            gros_penis = grosse_plote[tapette] 
        RammasisDeMarde += grosse_plote[tapette]
        tabarnak = RammasisDeMarde/len(grosse_plote)
    print("Le plus grand nombre est : " + str(gros_penis) + ", le plus petit nombre est : " + str(tit_penis) + ", la moyenne est : " + str(tabarnak) + ".")
caliss=[]
suce = int(input("Combien voulez-vous qu'il y aie de nombres? :"))
for fif in range(suce):
    caliss.append(float(input("Veuillez entrer le nombre " + str(fif + 1) +" : ")))
chienne(caliss)

    


                                        





