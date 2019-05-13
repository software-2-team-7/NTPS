class HookCollection(object):
    Hook_Collection_Name = ""
    Hook_Collection_Sequence_Number = 0
    Hook_Collection_Status = False
    Hook_Collection_Description = ""
    Hooks = [] #Hooks: List<Hook> 
    

    def __init__(self,name,seqNum,status,desc,h):
        self.Hook_Collection_Name = name
        self.Hook_Collection_Sequence_Number = seqNum
        self.Hook_Collection_Status = status
        self.Hook_Collection_Description = desc
        self.Hooks = h


    def knowIfHookSequenceIsUnique(self):
        print("A function")

    def knowIfHookCollectionSequenceIsUnique(self):
        print("A function")

    def searchHooks(self):
        print("A function")

    def executeHookSequence(self,packet):
        if (self.Hook_Collection_Status):
            newPacket = packet
            for h in self.Hooks:
                newPacket = h.execute(newPacket)
        return newPacket



    def updateHookSequencing(self): #private
        print("Hello!")

         
    def addHook(self,h): #private
        h.Hook_Association_Number+=1
        self.Hooks.append(h)
        
        

    def updateCollectionSequencing(self): #private
        print("Hello!")

    def removeHook(self): #private
        print("Hello")


    def insertionSort_Hook_Sequence_Number(self):
        for index in range(1,len(self.Hooks)):
            currentHook = self.Hooks[index]
            currentvalue = self.Hooks[index].Hook_Sequence_Number
            position = index
            while position>0 and self.Hooks[position-1].Hook_Sequence_Number > currentvalue:
                self.Hooks[position]=self.Hooks[position-1]
                position = position-1

            self.Hooks[position]=currentHook

    def getCollName(self):
        return self.Hook_Collection_Name
    
    def getCollSeqNum(self):
        return self.Hook_Collection_Sequence_Number
    
    def getCollStatus(self):
        return self.Hook_Collection_Status

    def getCollDesc(self):
        return self.Hook_Collection_Description
    
    def getHooks(self):
        return self.Hooks 





