import paramiko
import os

# 连接信息
host = '47.105.49.199'
port = 22
username = 'root'
password = 'Aliyun1993*lwS'

# 忽略的目录
skipArry = ['kai.xxxx.com', 'demo.xxxx.com']

fullpathArry = []
currentIndex = ''


# 判断文件是否存在
def judgeFileExist():
    global currentIndex
    # os.getcwd()函数获得当前的路径
    currentIndex = os.getcwd() + '/Index.php'
    # os.path.isfile(currentIndex)判断文件是否存在
    if os.path.isfile(currentIndex) == False:
        print('Index文件不存在')
        exit()
    print('文件检测成功,准备连接服务器...')


def creatConnect():
    try:
        print('开始连接服务器...')
        s = paramiko.Transport((host, port))
        s.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(s)
        print('连接:' + host + '成功')
        return sftp, s
    except Exception as e:
        print('连接服务器失败:' + str(e))


# 获取目录保存为数组
def getDirectory(sftp):
    print('开始获取目录...')
    # 切换工作陌路
    sftp.chdir('/root')
    pathlist = sftp.listdir(path='.')
    for path in pathlist:
        fullpath = '/root/' + path + '/application/index/controller'
        if path in skipArry:
            continue
        fullpathArry.append(fullpath)
    print('目录获取完毕')


# 上传Index文件
def uploadIndex(sftp):
    for fullpathitem in fullpathArry:
        remoteIndex = fullpathitem + '/Index.php'
        print('开始上传:' + remoteIndex)
        try:
            sftp.put(currentIndex, remoteIndex)
            try:
                sftp.file(remoteIndex)
                sftp.chmod(remoteIndex, int("775", 8))
                print('修改' + remoteIndex + '权限为755')
                print(fullpathitem + '上传成功')
            except:
                print(fullpathitem + '上传失败')
                continue
        except Exception as e:
            print('错误信息:' + str(e))
            continue


if __name__ == "__main__":
    judgeFileExist()
    sftp, s = creatConnect()
    getDirectory(sftp)
    uploadIndex(sftp)
    s.close()