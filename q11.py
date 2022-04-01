def converte_data(data):
    
    data_separada = data.split('/')
    
    lista1 = [1,2,3,4,5,6,7,8,9,10,11,12]
    lista2 = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    
    for i in range(len(lista1)):
        
        if(data_separada[1] == lista1[i]):
            
            lista1[i] = lista2[i]
            
    print(data_separada[0],"de", lista2[i],"de", data_separada[2],".")
            
    