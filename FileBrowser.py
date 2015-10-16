##test
##x=((x-500)/2)+500bin
import os
##path = "/tmp/home/monthly/daily"
##os.mkdir("newdir")#makes new dir
##os.chdir("newdir")#changes to new dir
##os.getcwd()##gets current dir
##os.makedirs( path, 0755 )##creates nested dirs
running = True
cmd = '/'
def quickrd(f):
 pass
os.chdir('/')
print(os.listdir())
while running:
    try:
        cmd = input('>')
        if cmd =='//o':##quickopen
            cmd = input('>>')
            f = open(cmd)
            while True:
                line = f.readline()
                if not line:
                    break
                print (line.strip('\n'))
            f.close()
        elif cmd == '//h':##help
            print('help menu')
            htxt = ['//o quick open','//h help menu','//q quit','//e execute','//s  searchcurrentdir','//rs recursive search','//fo fileoptions','//dsc drive detection']
            for x in htxt:
                print(x)
                 
        elif cmd == '//q':
            running = False
                #pass # do something
             
        elif cmd == '//e':##execute
            cmd = input('>>')
             
        elif cmd == '//s':##searchcurrdir
            cmd = input('>>')
            if cmd in os.listdir():
                print(cmd,'in current dir')
            else:
                print(cmd,'not in current dir')
 
            print('other results containing string: '+cmd)
            for x in range(len(os.listdir())):
                if cmd.lower() in os.listdir()[x].lower():
                    print('|',os.listdir()[x])
                 
                 
        elif cmd == '//rs':##recursivesrch
            cmd = input('>>')
             
        elif cmd == '//fo':#fileoptions
            print('readopen : r\nwritenewopen : o\nappendopen : a')
            cmd = input('>>')
            if cmd.lower() == 'r':
                pass
            elif cmd.lower() == 'o':
                cmd = input('>> are you sure?>y/n')
                if cmd.lower() == 'y':
                    pass#filestuff
                else:
                    print('cancelled.')
            elif cmd.lower() == 'a':
                pass
            else:
                print('invalid command')
                 
        elif cmd == '//dsc':#discoverdrive
            drvz=[]
            for x in range(65,91,1):##ascii a to z
                try:
                    print('drive:'+chr(x)+'\n',os.listdir(chr(x)+':'))
                    drvz.append(chr(x))
                     
                except:
                    print('no drive exists at',chr(x))
            print('existing drives',drvz)
                 
        else:
            tempselcf =[]
            tempcmdcf =''
            if os.listdir().lower().count() >1:#.lower may not work
                for item in os,listdir():
                    if item == cmd:
                        tempclf.append(item)
                        print('there are conflicts with the current selection\nplease choose the path you were trying to enter')
                        
                for x in range(0,len(tempselcf)):##need iterationint
                    print(str(x)+'.)  '+tempclf[x])
                    
            else:
               os.chdir(cmd)
               print(os.listdir())
    except:
        print('ERROR INVALID COMMAND',cmd,'\n',os.listdir())

