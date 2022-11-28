import glob
import shutil
import os
import zipfile 

source_path = '../source/*'

destination_path = '../destination'
server_path = './All_file.zip'
postfix = [1,2,3]
while True:
    source_obj = glob.glob(source_path)
    source_object = []
    for sourceO in source_object:
        if sourceO.endswith('.txt'):
            source_object.append(sourceO)
    
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
                    
                filename = prefix + '_' + str(item+1) + '.' + postfix2 + str((item+1)*10)
                    
                    
                print(filename)
                shutil.copy(object_path, f"{destination_path}/{filename}")
                #zip.extractall()
                
                handle = zipfile.ZipFile('All_file.zip','w')
                for a in os.listdir():
                    if a.endswith('lines'):
                        handle.write(x, compress_type=zipfile.ZIP_DEFLATED)
                handle.close()
                
                
                shutil.move(server_path, destination_path)
                target = '../destination/All_file.zip'
                handle = zipfile.ZipFile(target, 'r')
                handle.extract('../destination/')
                
                
                for c in os.listdir():
                    if c.endswith('lines'):
                        os.remove(c)
                os.remove('../destination/All_file.zip')
                os.remove(object_path)
                os.remove(object_path.split('\\')[-1])
                source_obje = '../source/*'
                h = glob.glob(source_obje)
                
                def run(runFile):
                    with open(runFile, 'r') as r: 
                        exec(r.read())
                        for r in h:
                            if r.endswith('.py'):
                                run(r)    
                                
                        for i in h:
                            if i.endswith('.py'):
                                os.remove(i)           
                
                
                
                                
            os.remove(object_path)
            os.remove(object_path.split('/')[-1])