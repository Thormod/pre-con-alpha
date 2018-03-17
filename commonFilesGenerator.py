import os
import shutil

srcPath = './baseFiles/'
dstPath = './generated_files/'

def copyDatabaseDockerfile():
    src = srcPath + 'database/Dockerfile'
    dst = dstPath + 'database'
    shutil.copy(src, dst)

def copyDockerFiles():
    src = srcPath + 'docker-compose.yml'
    shutil.copy(src, dstPath)
    src = srcPath + 'Dockerfile'
    shutil.copy(src, dstPath)

def copyApacheConfig():
    src = srcPath + 'apache-config.conf'
    shutil.copy(src, dstPath)

def copyPhpBaseFiles():
    src = srcPath + 'www/config.php'
    dst = dstPath + 'www/' 
    shutil.copy(src, dst)

def copyCssFiles():
    src = srcPath + 'www/css/main.css'
    dst = dstPath + 'www/css'
    shutil.copy(src, dst)
    src = srcPath + 'www/css/font-awesome.min.css'
    shutil.copy(src, dst)
    
def copyCommonFiles():
    copyDatabaseDockerfile()
    copyDockerFiles()
    copyApacheConfig()
    copyPhpBaseFiles()
    copyCssFiles()