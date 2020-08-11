from xml.etree import ElementTree
import csv
import os

def write_elements_info(listed,elements_info_save_path,ids, element_concat):
    
    text_file = open(elements_info_save_path, "w")
    text_file.writelines("---------------------------------------------------------------------------------\n")
    text_file.writelines("Detailed information of Elements: (Total files scanned = {})\n".format(ids))
    text_file.writelines("---------------------------------------------------------------------------------\n")
    
    list_of_elements=str()
    i =0
    for ele in listed:
        list_of_elements += ele
        MyList = ele.splitlines()
        MyList = list(dict.fromkeys(MyList))
        MyList = sorted(MyList)
        text_file.writelines("Elements in Level-{0}\n".format(i))
        text_file.writelines(["%s\n" % elist  for elist in MyList])
        text_file.writelines("Level-{0}, {1} Element/s Found \n\n".format(i,len(MyList)))
        i+=1

    MyList = list_of_elements.splitlines()
    MyList = list(dict.fromkeys(MyList))
    MyList = sorted(MyList)
    text_file.writelines("---------------------------------------------------------------------------------\n")
    text_file.writelines("List of Element\n")
    text_file.writelines("---------------------------------------------------------------------------------\n")
    text_file.writelines(["%s\n" % elist  for elist in MyList])
    text_file.writelines("Total of {0} Element/s Found \n\n".format(len(MyList)))
      
    MyList = element_concat.splitlines()
    MyList = list(dict.fromkeys(MyList))
    MyList = sorted(MyList)
    text_file.writelines("---------------------------------------------------------------------------------\n")
    text_file.writelines("Elements connectivity\n")
    text_file.writelines("---------------------------------------------------------------------------------\n")
    text_file.writelines(["%s\n" % elist  for elist in MyList])
    text_file.writelines("Total of {0} Element/s Connectivity Found \n\n".format(len(MyList)))

    text_file.close()



def main(import_directory_path,elements_info_save_path):
       
    root_element = first_level_elements = second_level_elements = third_level_elements = fourth_level_elements = str()
    fifth_level_elements = sixth_level_elements = seventh_level_elements = eighth_level_elements = nineth_level_elements = str()
    element_concat = str()

    xml_files = []
    # r= root, d=directories, f = files
    for r, d, f in os.walk(import_directory_path):
        for file in f:
            if '.xml' in file:
                xml_files.append(os.path.join(r, file))
    
    no_of_xml_files=len(xml_files)
    ids = 0   
    for f in xml_files:
        file_path = f
        ids+=1
        print(ids," of ",no_of_xml_files,"file scanning\n")
        
        tree = ElementTree.parse(file_path)
        root = tree.getroot()
        
        if root.tag not in root_element:
            root_element += str(root.tag+'\n',)
        if root.tag not in element_concat:
            element_concat += str(root.tag+'\n',)

        for level1_element in root:
            if level1_element.tag not in first_level_elements:
                first_level_elements += str(level1_element.tag+'\n',)
            level1_concat = root.tag + '//' + level1_element.tag
            if level1_concat not in element_concat:
                element_concat += str(level1_concat+'\n',)

            for level2_element in level1_element:
                if level2_element.tag not in second_level_elements:
                    second_level_elements += str(level2_element.tag+'\n',)
                level2_concat = level1_concat + '//' + level2_element.tag
                if level2_concat not in element_concat:
                    element_concat += str(level2_concat+'\n',)
                                    
                for level3_element in level2_element:
                    if level3_element.tag not in third_level_elements:
                        third_level_elements += str(level3_element.tag+'\n',)
                    level3_concat = level2_concat + '//' + level3_element.tag
                    if level3_concat not in element_concat:
                        element_concat += str(level3_concat+'\n',)
                                        
                    for level4_element in level3_element:
                        if level4_element.tag not in fourth_level_elements:
                            fourth_level_elements += str(level4_element.tag+'\n',)
                        level4_concat = level3_concat + '//' + level4_element.tag
                        if level4_concat not in element_concat:
                            element_concat += str(level4_concat+'\n',)
                        
                        for level5_element in level4_element:
                            if level5_element.tag not in fifth_level_elements:
                                fifth_level_elements += str(level5_element.tag+'\n',)
                            level5_concat = level4_concat + '//' + level5_element.tag
                            if level5_concat not in element_concat:
                                element_concat += str(level5_concat+'\n',)

                            for level6_element in level5_element:
                                if level6_element.tag not in sixth_level_elements:
                                    sixth_level_elements += str(level6_element.tag+'\n',)
                                level6_concat = level5_concat + '//' + level6_element.tag
                                if level6_concat not in element_concat:
                                    element_concat += str(level6_concat+'\n',)

                                for level7_element in level6_element:
                                    if level7_element.tag not in seventh_level_elements:
                                        seventh_level_elements += str(level7_element.tag+'\n',)
                                    level7_concat = level6_concat + '//' + level7_element.tag
                                    if level7_concat not in element_concat:
                                        element_concat += str(level7_concat+'\n',)
                                    
                                    for level8_element in level7_element:
                                        if level8_element.tag not in eighth_level_elements:
                                            eighth_level_elements += str(level8_element.tag+'\n',)
                                        level8_concat = level7_concat + '//' + level8_element.tag
                                        if level8_concat not in element_concat:
                                            element_concat += str(level8_concat+'\n',)
                                        
                                        for level9_element in level8_element:
                                            if level9_element.tag not in nineth_level_elements:
                                                nineth_level_elements += str(level9_element.tag+'\n',)
                                            level9_concat = level8_concat + '//' + level9_element.tag
                                            if level9_concat not in element_concat:
                                                element_concat += str(level9_concat+'\n',)

    listed = [root_element, first_level_elements, second_level_elements, third_level_elements, fourth_level_elements, fifth_level_elements, sixth_level_elements, seventh_level_elements, eighth_level_elements, nineth_level_elements]
        
    write_elements_info(listed,elements_info_save_path,ids, element_concat)
    
       
    
    print('Done')
    
    
if __name__ == "__main__":
    import_directory_path = r"\\192.168.6.8\Data_Science\ChemicalReactionPrediction\grants"
    #import_directory_path = r"D://python xml parsing//Grants"
    elements_info_save_path = import_directory_path+"//Elements_info.txt"
    main(import_directory_path,elements_info_save_path)

