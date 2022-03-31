from timeit 
import default_timer as timer 

def selection_sort(list): 
    start=timer()
    for i in range (len(list)): 
        small=i
        for j in range(i+1,len(list)):
            if list[small]>list[j]:
                small=j
                temporary=list[small]
                list[small]=list[i]
                list[i]=temporary
    end=timer() 
  
    print("Elapsed time for selection sort :",end-start)
    #sorting of the list and the execution time program code 
def insertion_sort(list):
    start=timer()
    for i in range(1,len(list)):
        k=list[i]
        h=i-1
        while k<list[h] and h>=0:
            list[h+1]=list[h]
            h=h-1
            list[h+1]=k
    end=timer()
    print("Elapsed time for insertion sort :",end-start) 


list1=[]
# open A.txt file and read
f1 = open("A.txt", "r")
for i in f1: 
   list1.append(int(i)) 
selection_sort(list1) 
insertion_sort(list1)
