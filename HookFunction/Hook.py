import importlib
import importlib.util

#Class definition for Hooks
class Hook(object):
    Hook_Name = "" #String
    Hook_Sequence_Number = 0 #Integer
    Boolean_Hook_Status = False #Boolean
    Hook_Description = "" #String
    Hook_Association_Number = 0 #Int
    hookPath = "" #String
    
    def __init__(self, hName, status, desc, seqNum, path):
        self.Hook_Name = hName
        self.Boolean_Hook_Status = status
        self.Hook_Description = desc
        self.Hook_Association_Number = 0
        self.Hook_Sequence_Number = seqNum
        self.hookPath = path
    

    def increment_association_number(self):
        print("Hello from a function")
        self.Hook_Association_Number = self.Hook_Association_Number + 1
        
    def decrement_association_number(self):
        print("Hello from a function")
        self.Hook_Association_Number =  self.Hook_Association_Number - 1

    def decrement_sequence_number(self):
        print("Hello from a function")
        self.Hook_Sequence_Number =  self.Hook_Sequence_Number - 1

    def setHookStatus(self):
        if (self.Hook_Sequence_Number):
            self.Hook_Sequence_Number = False
        else:
            self.Hook_Sequence_Number = True
        


    def execute(self, packet):
        print("Executing hook " + self.hookPath + "...")
        
        getFileName = self.hookPath.split("/")
        fileName = getFileName[len(getFileName)-1]

        if (self.Boolean_Hook_Status):
            
            #using importlib, import the script given by the client
            resource = importlib.util.spec_from_file_location(fileName, self.hookPath)
            script = importlib.util.module_from_spec(resource)
            resource.loader.exec_module(script) #initalize the script object
            #we create a varible storing and instance of the script class called 'run'
            run = script.run(packet)
            newPacket = run.execute() #we call the script's .execute() command and get the packet back
            print (newPacket)
            return newPacket #return the packet to the caller
    
    def getName(self):
        return self.Hook_Name

    def getSeqNum(self):
        return self.Hook_Sequence_Number

    def getStatus(self):
        return self.Boolean_Hook_Status
    
    def getDesc(self):
        return self.Hook_Description
    
    def getPath(self):
        return self.hookPath
    
    def getAssocNum(self):
        return self.Hook_Association_Number



            


            
            

            
        
