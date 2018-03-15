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
    src = srcPath + 'www/base.php'
    dst = dstPath + 'www/' 
    shutil.copy(src, dst)
    src = srcPath + 'www/config.php'
    shutil.copy(src, dst)

def copyCommonFiles():
    copyDatabaseDockerfile()
    copyDockerFiles()
    copyApacheConfig()
    copyPhpBaseFiles()