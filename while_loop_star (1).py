# triangle 
i=1

while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1
    
#  output
    
* 
* *
* * *
* * * *
* * * * *


# triangle

i=1

while i<=5:
    j=5
    while j>=i:
        print("*",end=" ")
        j-=1
    print()
    i+=1
    
#   output
    
* * * * * 
* * * *
* * *
* *
*


# triangle

i=1

while i<=5:
    j=2
    k=5
    
    while j<=i:
        print(" ",end=" ")
        j+=1
        
    while k>=i:
        print("*",end=" ")
        k-=1
        
    
    print()
    i+=1
    
    
# output    
    
* * * * * 
  * * * *
    * * *
      * *
        *
        
 
 

#triangle

i=1

while i<=5:
    j=4
    k=1
    
    while j>=i:
        print(" ",end=" ")
        j-=1
        
    while k<=i:
        print("*",end=" ")
        k+=1
        
    
    print()
    i+=1
    
# output

    
        * 
      * *
    * * *
  * * * *
* * * * *



#right half diamond pattern

i=1
while i<=6:
    j=1

    while j<=i:
        print("*",end=" ")
        j+=1
    
    print()
    
    i+=1

i=1
while i<=5:
    k=5
    while k>=i:
        print("*",end=" ")
        k-=1
    print()
    i+=1
    
#   output  
    
* 
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*


#left half diamond pattern

i=1

while i<=6:
    j=5
    k=1
    
    while j>=i:
        print(" ",end=" ")
        j-=1
        
    while k<=i:
        print("*",end=" ")
        k+=1
        
    
    print()
    i+=1
    
i=1

while i<=5:
    j=1
    k=5
    
    while j<=i:
        print(" ",end=" ")
        j+=1
        
    while k>=i:
        print("*",end=" ")
        k-=1
        
    
    print()
    i+=1
    
    
#    output 
    
          * 
        * *
      * * *
    * * * *
  * * * * *
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *
          
          

#full diamond pattern


i=1

while i<=7:
    j=6
    k=1
    
    while j>=i:
        print(" ",end="")
        j-=1
        
    while k<=i:
        print("*",end=" ")
        k+=1
        
    
    print()
    i+=2
    
i=1

while i<=5:
    j=0
    k=5
    
    while j<=i:
        print(" ",end="")
        j+=1
        
    while k>=i:
        print("*",end=" ")
        k-=1
        
    
    print()
    i+=2
    
    
    
# output

      * 
    * * *
  * * * * *
* * * * * * *
  * * * * *
    * * *
      *
     
     

# solid rhombus right inclined


i=1
while i<=5:
    j=4
    k=1
    while j>=i:
        print(" ",end=" ")
        j-=1
    while k<=5:
        print("*",end=" ")
        k+=1
    print()
    i+=1
    
#  output   
 
         * * * * * 
      * * * * *
    * * * * *
  * * * * *
* * * * *



# solid rhombus left inclined


i=1
while i<=5:
    j=2
    k=1
    while j<=i:
        print(" ",end=" ")
        j+=1
    while k<=5:
        print("*",end=" ")
        k+=1
    print()
    i+=1
    
    output

* * * * * 
  * * * * *
    * * * * *
      * * * * *
        * * * * *
        

# solid rectangle


i=1
while i<4:
    j=1
    while j<5:
        print("*",end=" ")
        j+=1
    
    print()
    i+=1
    
output

* * * * 
* * * *
* * * *
``

`
# butterfly pattern

i=1

while i<=7:
    j=1
    k=6
    l=1
    while j<=i:
        print("*",end=" ")
        j+=1
    while k>=i:
        print("   ",end=" ")
        k-=1
    while l<=i:
        print("*",end=" ")
        l+=1
    print()
    i+=1

i=1
while i<=6:
    j=6
    k=1
    l=6
    while j>=i:
        print("*",end=" ")
        j-=1
    while k<=i:
        print("   ",end=" ")
        k+=1
    while l>=i:
        print("*",end=" ")
        l-=1
    print()
    i+=1
    
    # output
    
*                         * 
* *                     * *
* * *                 * * *
* * * *             * * * *
* * * * *         * * * * *
* * * * * *     * * * * * *
* * * * * * * * * * * * * *
* * * * * *     * * * * * *
* * * * *         * * * * *
* * * *             * * * *
* * *                 * * *
* *                     * *
*                         *
```

# hollow rectangle

i=1
while i<=3:
    j=1
    while j <=5:
        if i==1 or i==3:
            print("*",end=" ")
        else:
            while j<=5:
                if j==1 or j==5:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                j+=1
                
        j+=1
    print()
    i+=1
    
#    output 
    
* * * * * 
*       *
* * * * *
```