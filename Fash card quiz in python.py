
import random
dict = {
    "WATER":["pink","red","blue",2],
    "SUN":["black","yellow","green",1],
    "MOON":["white","orange","purple",0]
    }
listofkeys = list(dict.keys())
random.shuffle(listofkeys)
print("pick the right option of the following:-")
correct = 0
wrong = 0
for i in listofkeys:
    sf = "What color is {} \nA){} \nB){} \nC){}"
    print()
    print(sf.format(i,dict[i][0],dict[i][1],dict[i][2]))
    letter =input("Enter your choice either A) either B) or C)").upper()
    if letter == "ABC"[dict[i][3]]:
        print("CORRECT")
        correct+=1
    else:
        print("WRONG")
        wrong+=1

ans = "Result----->correct {},wrong{}"
print(ans.format(correct,wrong))
    
