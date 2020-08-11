from xml.etree import ElementTree
import csv
import os

'''
# Spec-1
def source(root, savePath, csv_writer):
    sourceData = ['UNIQUEID', 'TEXTUAL_DESCRIPTION_OF_REACTION', 'REACTION_SMILES']
    csv_writer.writerow(sourceData)
    for reactionList in root:
        Reaction_Smiles = 'NA'
        for reaction in reactionList:
            if reaction.tag == "{http://bitbucket.org/dan2097}source":
                Text = ''
                UniqueId = 'NA'
                Textual_Description_Of_Reaction ='NA'
                for source in reaction:
                    if source.tag == "{http://bitbucket.org/dan2097}documentId":
                        UniqueId = source.text
                    if source.tag == "{http://bitbucket.org/dan2097}headingText":
                        Text += source.text + "\n"
                    if source.tag == "{http://bitbucket.org/dan2097}paragraphText":
                        Text += source.text
                Textual_Description_Of_Reaction = Text
            if reaction.tag == "{http://bitbucket.org/dan2097}reactionSmiles":
                Reaction_Smiles = reaction.text
        sourceData = [UniqueId, Textual_Description_Of_Reaction, Reaction_Smiles]
        csv_writer.writerow(sourceData)
        #break;

# Spec-2    
def productList(root, savePath, csv_writer):
    productListData = ['UNIQUEID','TEXTUAL_DESCRIPTION_OF_REACTION','ROLE','ENTITY','SMILES','InChI','ENTITY_TYPE','MOLECULE_ID','ENTITY_SYNONYMS']
    csv_writer.writerow('\n')
    csv_writer.writerow(productListData)    
    for reactionList in root:
        for reaction in reactionList:
            if reaction.tag == "{http://bitbucket.org/dan2097}source":
                Text = ''
                UniqueId  = 'NA'
                Textual_Description_Of_Reaction = 'NA'
                for source in reaction:
                    if source.tag == "{http://bitbucket.org/dan2097}documentId":
                        UniqueId = source.text
                    if source.tag == "{http://bitbucket.org/dan2097}headingText":
                        Text += source.text + "\n"
                    if source.tag == "{http://bitbucket.org/dan2097}paragraphText":
                        Text += source.text
                Textual_Description_Of_Reaction = Text
                
            if reaction.tag == "{http://www.xml-cml.org/schema}productList":        
                for productList in reaction:
                    if productList.tag == "{http://www.xml-cml.org/schema}product":
                        if productList.attrib == {}:
                            Product_Role = 'NA'
                        else :
                            Product_Role = productList.attrib['role']
                        Product_InChI = 'NA'
                        Product_Smile = 'NA'
                        Product_Entity_Type = 'NA'
                        Product_Molecule_Id = 'NA'
                        for product in productList:
                            if product.tag == "{http://www.xml-cml.org/schema}molecule":
                                Product_Molecule_Id = product.attrib['id']
                                Product_Entity = 'NA'
                                Product_Entity_Synonyms = 'NA'
                                for molecule in product:  
                                    if molecule.tag == "{http://www.xml-cml.org/schema}name":
                                        Product_Entity = molecule.text
                                    if molecule.tag == "{http://bitbucket.org/dan2097}nameResolved":
                                        Product_Entity_Synonyms = molecule.text                           
                            if product.tag == "{http://www.xml-cml.org/schema}identifier":
                                if product.attrib['dictRef'] == 'cml:inchi':
                                    Product_InChI = product.attrib['value']
                                if product.attrib['dictRef'] == 'cml:smiles':
                                    Product_Smile = product.attrib['value']
                            if product.tag == "{http://bitbucket.org/dan2097}entityType":
                                Product_Entity_Type = product.text
                        productListData = [UniqueId, Textual_Description_Of_Reaction,Product_Role, Product_Entity, Product_Smile, Product_InChI, Product_Entity_Type, Product_Molecule_Id, Product_Entity_Synonyms]
                        csv_writer.writerow(productListData)
        #break;                              

# Spec-3
def reactantList(root, savePath, csv_writer):
    reactantListData = ['UNIQUEID','TEXTUAL_DESCRIPTION_OF_REACTION','ROLE','ENTITY','SMILES','InChI','ENTITY_TYPE','MOLECULE_ID']
    csv_writer.writerow('\n')
    csv_writer.writerow(reactantListData)    
    for reactionList in root:
        for reaction in reactionList:
            if reaction.tag == "{http://bitbucket.org/dan2097}source":
                Text = ''
                UniqueId = 'NA'
                Textual_Description_Of_Reaction = 'NA'
                for source in reaction:
                    if source.tag == "{http://bitbucket.org/dan2097}documentId":
                        UniqueId = source.text
                    if source.tag == "{http://bitbucket.org/dan2097}headingText":
                        Text += source.text + "\n"
                    if source.tag == "{http://bitbucket.org/dan2097}paragraphText":
                        Text += source.text
                Textual_Description_Of_Reaction = Text
                
            if reaction.tag == "{http://www.xml-cml.org/schema}reactantList":        
                for reactantList in reaction:
                    if reactantList.tag == "{http://www.xml-cml.org/schema}reactant":
                        if reactantList.attrib == {}:
                            Reactant_Role = 'NA'
                        else :
                            Reactant_Role = reactantList.attrib['role']
                        Reactant_InChI = 'NA'
                        Reactant_Smile = 'NA'
                        Reactant_Molecule_Id = 'NA'
                        Reactant_Entity_Type = 'NA'
                        for reactant in reactantList:
                            if reactant.tag == "{http://www.xml-cml.org/schema}molecule":
                                Reactant_Molecule_Id = reactant.attrib['id']
                                Reactant_Entity = 'NA'
                                Reactant_Entity = 'NA'
                                for molecule in reactant: 
                                    if molecule.tag == "{http://www.xml-cml.org/schema}name":
                                        Reactant_Entity = molecule.text                          
                            if reactant.tag == "{http://www.xml-cml.org/schema}identifier":
                                if reactant.attrib['dictRef'] == 'cml:inchi':
                                    Reactant_InChI = reactant.attrib['value']
                                if reactant.attrib['dictRef'] == 'cml:smiles':
                                    Reactant_Smile = reactant.attrib['value']
                            if reactant.tag == "{http://bitbucket.org/dan2097}entityType":
                                Reactant_Entity_Type = reactant.text
                        reactantListData = [UniqueId, Textual_Description_Of_Reaction,Reactant_Role, Reactant_Entity, Reactant_Smile, Reactant_InChI, Reactant_Entity_Type, Reactant_Molecule_Id]
                        csv_writer.writerow(reactantListData)          
        #break;                              

# Spec-4
def spectatorList(root, savePath, csv_writer):
    spectatorListData = ['UNIQUEID','TEXTUAL_DESCRIPTION_OF_REACTION','ROLE','ENTITY','SMILES','InChI','ENTITY_TYPE','MOLECULE_ID']
    csv_writer.writerow('\n')
    csv_writer.writerow(spectatorListData)    
    for reactionList in root:
        for reaction in reactionList:
            if reaction.tag == "{http://bitbucket.org/dan2097}source":
                Text = ''
                UniqueId = 'NA'
                Textual_Description_Of_Reaction = 'NA'
                for source in reaction:
                    if source.tag == "{http://bitbucket.org/dan2097}documentId":
                        UniqueId = source.text
                    if source.tag == "{http://bitbucket.org/dan2097}headingText":
                        Text += source.text + "\n"
                    if source.tag == "{http://bitbucket.org/dan2097}paragraphText":
                        Text += source.text
                Textual_Description_Of_Reaction = Text
                
            if reaction.tag == "{http://www.xml-cml.org/schema}spectatorList":        
                for spectatorList in reaction:
                    if spectatorList.tag == "{http://www.xml-cml.org/schema}spectator":
                        if spectatorList.attrib == {}:
                            Spectator_Role = 'NA'
                        else :
                            Spectator_Role = spectatorList.attrib['role']
                        Spectator_InChI = 'NA'
                        Spectator_Smile = 'NA'
                        Spectator_Molecule_Id = 'NA'
                        Spectator_Entity_Type = 'NA'
                        for spectator in spectatorList:
                            if spectator.tag == "{http://www.xml-cml.org/schema}molecule":
                                Spectator_Molecule_Id = spectator.attrib['id']
                                Spectator_Entity = 'NA'
                                for molecule in spectator:
                                    if molecule.tag == "{http://www.xml-cml.org/schema}name":
                                        Spectator_Entity = molecule.text                          
                            if spectator.tag == "{http://www.xml-cml.org/schema}identifier":
                                if spectator.attrib['dictRef'] == 'cml:inchi':
                                    Spectator_InChI = spectator.attrib['value']
                                if spectator.attrib['dictRef'] == 'cml:smiles':
                                    Spectator_Smile = spectator.attrib['value']
                            if spectator.tag == "{http://bitbucket.org/dan2097}entityType":
                                Spectator_Entity_Type = spectator.text
                        spectatorListData = [UniqueId, Textual_Description_Of_Reaction,Spectator_Role, Spectator_Entity, Spectator_Smile, Spectator_InChI, Spectator_Entity_Type, Spectator_Molecule_Id]
                        csv_writer.writerow(spectatorListData)
        #break;       


'''
# Spec-5
def reactionActionList(root, savePath, csv_writer):
    reactionActionListData = ['UNIQUEID','TEXTUAL_DESCRIPTION_OF_REACTION','ROLE','ENTITY','SMILES','InChI','ENTITY_TYPE','MOLECULE_ID', 'ENTITY_SYNONYMS', 'PHRASE_TEXT', 'CHEMICAL_REF', 'ACTION', 'TIME', 'TEMPERATURE','PRESSURE', 'STATE', 'VOLUME', 'MASS']
    csv_writer.writerow('\n')
    csv_writer.writerow(reactionActionListData)    
    for reactionList in root:
        for reaction in reactionList:
            if reaction.tag == "{http://bitbucket.org/dan2097}source":
                Text = ''
                UniqueId = 'NA'
                Textual_Description_Of_Reaction = 'NA'
                for source in reaction:
                    if source.tag == "{http://bitbucket.org/dan2097}documentId":
                        UniqueId = source.text
                    if source.tag == "{http://bitbucket.org/dan2097}headingText":
                        Text += source.text + "\n"
                    if source.tag == "{http://bitbucket.org/dan2097}paragraphText":
                        Text += source.text
                Textual_Description_Of_Reaction = Text
                
            if reaction.tag == "{http://bitbucket.org/dan2097}reactionActionList":        
                for reactionActionList in reaction:
                    #print(reactionActionList.tag)
                    if reactionActionList.tag == "{http://bitbucket.org/dan2097}reactionAction":
                        #print(reactionActionList.attrib)
                        if reactionActionList.attrib == {}:
                            ReactionAction_Action = 'NA'
                        else :
                            ReactionAction_Action = reactionActionList.attrib['action']

                        ReactionAction_PhraseText = 'NA'
                        Chemical_Ref = ''
                        Time = 'NA'
                        Temperature = ''
                        Pressure = 'NA'
                        ReactionAction_Role = 'NA'


                                                                              
                        ReactionAction_Molecule_Id = 'NA'
                        ReactionAction_Entity = 'NA'
                        ReactionAction_Entity_Type = 'NA'
                        ReactionAction_Smile = 'NA'
                        ReactionAction_InChI = 'NA'
                        ReactionAction_Entity_Synonyms = 'NA'
                        State = 'NA'
                        Volume = 'NA'
                        Mass = 'NA'

                        i=0
                        for reactionAction in reactionActionList:
                            #print(reactionAction.tag)
                            if reactionAction.tag == "{http://bitbucket.org/dan2097}phraseText":
                                ReactionAction_PhraseText = reactionAction.text



                            if reactionAction.tag == "{http://bitbucket.org/dan2097}chemical":
                                #print(reactionAction.tag, reactionAction.attrib)
                                Chemical_Ref += reactionAction.attrib['ref'] + '|'
                            
##########################################
                            if reactionAction.tag =="{http://www.xml-cml.org/schema}chemical":
                                i+=1
                                #print(reactionAction.tag, reactionAction.attrib)
                                if reactionAction.attrib == {}:
                                    ReactionAction_Role = 'NA'
                                else :
                                    ReactionAction_Role = reactionAction.attrib['role']
                                #print(ReactionAction_Role)


                                
                                ReactionAction_Molecule_Id = 'NA'
                                ReactionAction_Entity = 'NA'
                                ReactionAction_Entity_Synonyms ='NA'
                                ReactionAction_InChI = 'NA'
                                ReactionAction_Smile = 'NA'
                                ReactionAction_Entity_Type = 'NA'
                                State = 'NA'
                                Volume = 'NA'
                                Mass = 'NA'
                                for chemical in reactionAction:
                                    #print(chemical.tag)
                                    if chemical.tag == "{http://www.xml-cml.org/schema}molecule":
                                        ReactionAction_Molecule_Id = chemical.attrib['id']
                                        
                                        for molecule in chemical:
                                            if molecule.tag == "{http://www.xml-cml.org/schema}name":
                                                ReactionAction_Entity = molecule.text
                                            if molecule.tag == "{http://bitbucket.org/dan2097}nameResolved":
                                                ReactionAction_Entity_Synonyms = molecule.text
                                    if chemical.tag == "{http://www.xml-cml.org/schema}identifier":
                                        if chemical.attrib['dictRef'] == 'cml:inchi':
                                            ReactionAction_InChI = chemical.attrib['value']
                                        if chemical.attrib['dictRef'] == 'cml:smiles':
                                            ReactionAction_Smile = chemical.attrib['value']
                                    if chemical.tag == "{http://bitbucket.org/dan2097}entityType":
                                        ReactionAction_Entity_Type = chemical.text
                                    if chemical.tag == "{http://bitbucket.org/dan2097}state":
                                        State = chemical.text
                                    if chemical.tag == "{http://www.xml-cml.org/schema}amount":
                                        if chemical.attrib['{http://bitbucket.org/dan2097}propertyType'] == 'VOLUME':
                                            Volume = chemical.text
                                        if chemical.attrib['{http://bitbucket.org/dan2097}propertyType'] == 'MASS':
                                            Mass = chemical.text
                            ###########################        
                            if reactionAction.tag == "{http://bitbucket.org/dan2097}parameter":
                                #print(reactionAction.tag, reactionAction.attrib)
                                if reactionAction.attrib['propertyType'] == 'Time':
                                    #print(reactionAction.text)
                                    Time = reactionAction.text
                                    #print(R_Time)
                                if reactionAction.attrib['propertyType'] == 'Temperature':
                                    Temperature += reactionAction.text + '|'
                                if reactionAction.attrib['propertyType'] == 'Pressure':
                                    Pressure = reactionAction.text
                            
                           #print(R_Time)
                        if Chemical_Ref == '':
                            Chemical_Ref = 'NA'
                        else:
                            Chemical_Ref = Chemical_Ref[:-1]
                        if Temperature == '':
                            Temperature ='NA'
                        else:
                            Temperature = Temperature[:-1]
  
                        reactionActionListData = [UniqueId, Textual_Description_Of_Reaction,ReactionAction_Role, ReactionAction_Entity, ReactionAction_Smile, ReactionAction_InChI, ReactionAction_Entity_Type, ReactionAction_Molecule_Id, ReactionAction_Entity_Synonyms, ReactionAction_PhraseText, Chemical_Ref, ReactionAction_Action, Time, Temperature, Pressure, State, Volume, Mass]    
                            #print(reactionActionListData)
                        csv_writer.writerow(reactionActionListData)                               
                        
                        #break;       



'''
# Spec-5 old
def reactionActionList(root, savePath, csv_writer):
    reactionActionListData = ['UNIQUEID','TEXTUAL_DESCRIPTION_OF_REACTION','ROLE','ENTITY','SMILES','InChI','ENTITY_TYPE','MOLECULE_ID']
    csv_writer.writerow('\n')
    csv_writer.writerow(reactionActionListData)    
    for reactionList in root:
        for reaction in reactionList:
            if reaction.tag == "{http://bitbucket.org/dan2097}source":
                Text = ''
                UniqueId = 'NA'
                Textual_Description_Of_Reaction = 'NA'
                for source in reaction:
                    if source.tag == "{http://bitbucket.org/dan2097}documentId":
                        UniqueId = source.text
                    if source.tag == "{http://bitbucket.org/dan2097}headingText":
                        Text += source.text + "\n"
                    if source.tag == "{http://bitbucket.org/dan2097}paragraphText":
                        Text += source.text
                Textual_Description_Of_Reaction = Text
                
            if reaction.tag == "{http://bitbucket.org/dan2097}reactionActionList":        
                for reactionActionList in reaction:
                    if reactionActionList.tag == "{http://bitbucket.org/dan2097}reactionAction":
                        if reactionActionList.attrib == {}:
                            ReactionAction_Role = 'NA'
                        else :
                            ReactionAction_Role = reactionActionList.attrib['action']

                        ReactionAction_Entity = 'NA'
                        ReactionAction_Molecule_Id = ''
                        for reactionAction in reactionActionList:
                            if reactionAction.tag == "{http://bitbucket.org/dan2097}phraseText":
                                ReactionAction_Entity = reactionAction.text
                            if reactionAction.tag == "{http://bitbucket.org/dan2097}chemical":
                                if reactionAction.attrib =={}:
                                    ReactionAction_Molecule_Id += ''
                                else:
                                    ReactionAction_Molecule_Id += reactionAction.attrib['ref'] + '|'

                            ReactionAction_InChI = 'NA'
                            ReactionAction_Smile = 'NA'                      
                            ReactionAction_Entity_Type ='NA'
                            for chemical in reactionAction:
                                if chemical.tag == "{http://www.xml-cml.org/schema}identifier":
                                    if chemical.attrib['dictRef'] == 'cml:inchi':
                                        ReactionAction_InChI = chemical.attrib['value']
                                    if chemical.attrib['dictRef'] == 'cml:smiles':
                                        ReactionAction_Smile = chemical.attrib['value']
                                if chemical.tag == "{http://bitbucket.org/dan2097}entityType":
                                    ReactionAction_Entity_Type = chemical.text

                        if ReactionAction_Molecule_Id == '':
                            ReactionAction_Molecule_Id = 'NA'
                        else:
                            ReactionAction_Molecule_Id = ReactionAction_Molecule_Id[:-1]

                        reactionActionListData = [UniqueId, Textual_Description_Of_Reaction,ReactionAction_Role, ReactionAction_Entity, ReactionAction_Smile, ReactionAction_InChI, ReactionAction_Entity_Type, ReactionAction_Molecule_Id]
                        csv_writer.writerow(reactionActionListData)  
        #break;       

'''
#main
def main():


    '''
    importDirectoryPath = r"//192.168.6.8/Data_Science/ChemicalReactionPrediction/grants"
    saveDirectoryPath = importDirectoryPath + '(CSV)'

    xmlFiles = []
    # r= root, d=directories, f = files
    for r, d, f in os.walk(importDirectoryPath):
        #print(f)
        saveDirectory = r.replace(importDirectoryPath,saveDirectoryPath)
        #os.mkdir(saveDirectory)
        for file in f:
            print(file)
            if '.xml' in file:
                xmlFiles.append(os.path.join(r, file))
                
    for f in xmlFiles:
        filePath = f
        savePath = filePath.replace(importDirectoryPath, saveDirectoryPath)
        savePath = savePath.replace('.xml', '.csv')
        #print(filePath)
        #print(savePath)
        
        tree = ElementTree.parse(filePath)
        root = tree.getroot()
        
        with open(savePath, 'w', newline='', encoding='utf-8') as write_obj:
            csv_writer = csv.writer(write_obj, delimiter='\t')
            
            source(root, savePath, csv_writer)
            productList(root, savePath, csv_writer)
            reactantList(root, savePath, csv_writer)
            spectatorList(root, savePath, csv_writer)
            reactionActionList(root, savePath, csv_writer)
    '''
    
    # for one file
    
    FilePath = "D://pftaps19760203_wk05.xml"
    savePath = "D://pftaps19760203_wk05.csv"
    
    tree = ElementTree.parse(FilePath)
    root = tree.getroot()
    
    with open(savePath, 'w', newline='', encoding='utf-8') as write_obj:
        csv_writer = csv.writer(write_obj, delimiter='\t')

        #source(root, savePath, csv_writer)
        #productList(root, savePath, csv_writer)
        #reactantList(root, savePath, csv_writer)
        #spectatorList(root, savePath, csv_writer)
        reactionActionList(root, savePath, csv_writer)   
    
    
    print('Done')
    
    
if __name__ == "__main__":
    main()
