import random 


while True:
    val = input("1-Play\n2-Exit\n: ")
    if val == "1":
        liste = [0,1,2,3,4,5,6,7,8,9]

        newlist = []
        arc = random.choice(liste)
        while True:
            if arc != 0:
                newlist.append(arc)
                break

        x = 0
        while x < 3:
            val = random.choice(liste)
            if val not in newlist:
                newlist.append(val)
                x += 1
            if val in newlist:
                continue

        piles = ""
        for i in newlist:
            piles += str(i)
            
        mylist = []
        for i in piles:
            mylist.append(i)


        while True:
            
            
            error = []
            while True:
                arc = input("Type a number: ")
                try:
                    arc = int(arc)
                    break
                except Exception:
                    print("Type numbers only!")
            
            for i in str(arc):
                if str(arc).count(i) > 1:
                    error.append(i)
            
            

            if int(arc) < 1000 or int(arc) > 9999:
                print("The number should be 4 digit")
            else:
                if len(error) > 0 :
                    print("You should type with using different numbers!")

            
                
                if len(error) == 0 :
                    
                    newlist = []
                    arc = str(arc)
                    for i in arc:
                        newlist.append(i)

                    count = []
                    for i in arc:
                        if i in mylist:
                            indexVal = mylist.index(i)
                            indexArc = newlist.index(i)
                            if indexVal == indexArc:
                                count.append(1)
                            elif indexVal != indexArc:
                                count.append(-1)
                    newcount = []
                    pile = 0
                    pileNegative = 0
                    for element in count:
                        if element > 0:
                            pile += element
                        elif element < 0:
                            pileNegative += element

                    newcount.append(pile)
                    newcount.append(pileNegative)
                    for i in newcount:
                        if i == 0:
                            newcount.remove(i)
                    if newcount[0] == 4:
                        print(f"Congratulations! The numbers was {piles}!")

                        break
                    print(newcount)
        
                


    elif val == "2":
        break
    else:
        print("Please type correctly!")






