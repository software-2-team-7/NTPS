class HookCollectionManager(object):
    collection = []
    hooks = []

    def __init__(self,collect,hook):
        self.collection = collect 
        self.hooks = hook
    
    def executeCollection(self,packet):
        newPacket = packet
        for h in self.collection:
            newPacket = h.executeHookSequence(newPacket)
        return newPacket

    def insertionSort_Hook_Collection_Sequence_Number(self):
        for index in range(1,len(self.collection)):
            currentHookCollection = self.collection[index]
            currentvalue = self.collection[index].Hook_Collection_Sequence_Number
            position = index
            while position>0 and self.collection[position-1].Hook_Collection_Sequence_Number > currentvalue:
                self.collection[position]=self.collection[position-1]
                position = position-1

            self.collection[position]=currentHookCollection

    def deleteCollection(self):
        print("Collection deleted.")
    
    def deleteHook(self):
        print("Hello!")
    
    def addHookCollection(self,c):
        self.collection.append(c)
    
    def addHook(self,h):
        self.hooks.append(h)
    
    def getCollections(self):
        return self.collection
    
    def getHooks(self):
        return self.hooks


    

