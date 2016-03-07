#ziplib

##def unzip(source_filename, dest_dir):
##    with zipfile.ZipFile(source_filename) as zf:
##        for member in zf.infolist():
##            zf.extract(member, dest_dir)

##def unzip(source_filename, dest_dir):
##    with zipfile.ZipFile(source_filename) as zf:
##        zf.extractall(dest_dir)

##import zipfile
##with zipfile.ZipFile("ds_dphs_csv.zip") as a:
##        a.extractall()
import zipfile,os
def ext2dir(fname,dname):
    zipfl = zipfile.ZipFile(os.getcwd()+'\\'+fname+".zip")
    os.mkdir(str(dname))
    os.chdir(str(dname))
#    with  as a:
    zipfl.extractall()
    
def extract_all():
    with zipfile.ZipFile("ds_dphs_csv.zip") as a:
        a.extractall()
##testing push system
