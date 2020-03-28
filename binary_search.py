def bs(data,item, low, high):
    if (low > high):
        return 0
    else :
        mid = (low + high )//2
        if(item == data[mid]):
           return mid;
           
        elif(item < data[mid]):
           return bs(data,item,low,mid-1)
           
        else:
           return bs(data,item,mid+1,high)



data=[1,3,5,6,7,9,10,14,17,19]
n=10
location=bs(data,17,0,n-1)
print(location)
 
