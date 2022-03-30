def print_seq(n, same_output = True):

    for i in range(1, n+1):
        
        if same_output == True: 

            to_print = [i]*i

        else:
            
            to_print = list(range(1, i+1))

        for j in to_print:

            print(j, end = " ")
        
        print(" ")


print_seq(10)

        

    
   
