
while(True):
    
    table = {}

    x = raw_input("Input Command: ")

    if(x == "help"):
        print "e for clean exit"
        print "q 'item' for query"
        print "a item::location for add"

    if(x == "e"):
        break
    w = x.split("q ")
    if(len(w) > 1):

        f = open("Table.txt","r")
        try:
            table =  eval(f.read())
        except:
            print "Table is Empty or There is an error"
        f.close()

        try:
            print table[w[1]]
        except:
            print "Item not found, check spelling"
        x = ""
    w = x.split("a ")
    if(len(w)> 1):

        f = open("Table.txt","r")
        try:
            table = eval(f.read())
        except:
            print "Table is Empty or There is an error"
        f.close()
        f = open("Table.txt","w").close()

        z = w[1].split("::")
        table[z[0]] = z[1]
        
        f = open("Table.txt","w")
        f.write(str(table))
        f.close()
        x = ""
    

        
        

        
