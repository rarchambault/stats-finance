#def toMiles(km):
    #miles = km * 0.6214
    #return miles

#value = float(input("Enter a value in kilometers: ")) 
#result = round(toMiles(value),2)
#output = str(value) + " kilometers equals " + str(result) + " miles."
#print(output)

#def toTime(i):
    #minutes = int(i/60)
    #seconds = int(i%60)
    #hours = int(minutes/60)
    #result = str(hours) + " hour(s) :: " + str(minutes) + " minute(s) :: " + str(seconds) + " second(s)"
    #return result

#value = int(input("Enter a time in seconds: "))
#output = toTime(value)
#print(output)

#n = list(map(int, input("elements of array:-").strip().split()))

#def number_stats(a):
    #smallest = 0
    #largest = 0
    #sum = 0
    #average = 0
    #for i in range(0,len(a)):
        #if(i == 0 or a[i] < smallest): smallest = a[i]
        #if(a[i]>largest): largest = a[i]
        #sum += a[i]
        #average = round(sum/len(a),2)
    #print("The smallest number is " + str(smallest) + ", the largest number is " + str(largest) + ", and the average is " + str(average) + ".")


#n=int(input("Number of elements in array:"))
#a=[]
#for i in range(0,n):
#   l=int(input("Enter number: "))
#   a.append(l)
#number_stats(a)
   
def toBinary(i):
    rest = int(i/2)
    bit = i%2
    result = str(bit)
    i = rest
    while (rest > 0):
        rest = int(i/2)
        bit = i%2
        result += str(bit)
        i = rest
    result = result[::-1]
    return result
   
n = int(input("Enter a positive number: "))
output = toBinary(n)
print(str(n) + " in binary notation is " + str(output) + ".")
