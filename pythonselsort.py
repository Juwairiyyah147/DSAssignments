Arr = [] 
n = int(input("Enter number of elements "))
  
for i in range(0, n):
    arrayelement = int(input())  
    Arr.append(arrayelement) 
      
print("the unsorted array is ",Arr)



def selsort(Arr,n):
    for i in range(n-1):
        min = i 
        for j in range(i+1, n):
            if Arr[j] < Arr[min]:
                min = j 
              
       
        tmp=Arr[min]
        Arr[min]=Arr[i]
        Arr[i]=tmp
  

    print ("Sorted array is" ,Arr) 

selsort(Arr,n)
