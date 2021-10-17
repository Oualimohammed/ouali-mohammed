# thuisoef 1 
# thuis oefening 1 
def zijn_gelijk(list_A, list_B):
    for element in list_A:
        if element in list_B:
            return True
        else:
            return False 

list_getallen_A = [10, 14, 2, 3, -10]
list_getallen_B = [-10,3,2,10,14]
resultaat= zijn_gelijk(list_getallen_A , list_getallen_B)


if resultaat ==True:
    print("true")
else:
    print("fals")




