import glob
import shutil
import os
import zipfile 

source_path = '../source/*'

destination_path = '../destination'
postfix = [1,2,3]
while True:
    source_object = glob.glob(source_path)
    
    if len(source_object) > 0:

       

        
        #print(source_object)

        object_path = source_object[0]
        shutil.copy(object_path, '.')

        object_name = object_path.split('\\')[-1].split('.')
        #print(object_name)
        prefix = object_name[0]
        postfix2 = object_name[1]



        '''file = open('some.txt', 'r')
        count = 0
        content = file.read()
        lines = content.split('.')
        for line in lines:
            if line:
                count += 1
        #print(count)'''
            
            
            

        for item in range(len(postfix)):
            #print(item)
            
            
            '''with open('some.txt', 'r') as f:
                    lines = f.readlines(split('.'))
                    for line in lines:
                        print(line)  
            
            '''
                
            #with zipfile.ZipFile("sample.zip", mode="r") as archive:
                
            filename = prefix + '_' + str(item+1) + '.' + postfix2
                
                
            print(filename)
            shutil.copy(object_path, f"{destination_path}/{filename}")
            #zip.extractall()
            
        os.remove(object_path)
        os.remove(object_path.split('/')[-1])