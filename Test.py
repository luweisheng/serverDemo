import paramiko
import os

# # http://192.168.188.99:20005/
# host = '47.105.49.199'
# port = 22
# username = 'root'
# password = 'Aliyun1993*lwS'


class Server_code_update():
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        # 忽略的目录
        self.skipArry = ['kai.xxxx.com', 'demo.xxxx.com']
        # 服务器代码目录汇总
        self.fullpathArry = []
        # 新代码文件
        self.currentIndex = 'D:/odoo/serverDemo/index.html'

    # 服务器连接
    def connect_server(self):
        try:
            print('开始连接服务器...')
            s = paramiko.Transport((self.host, self.port))
            s.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(s)
            print('连接:' + self.host + '成功')
            return sftp, s
        except Exception as e:
            print('连接服务器失败:' + str(e))

    # 获取服务器文件目录
    def getDirectory(self, sftp):
        print('开始获取目录...')
        # 切换工作陌路
        sftp.chdir('/root')
        pathlist = sftp.listdir(path='.')
        for path in pathlist:
            if path[0] =='.':
                continue
            fullpath = '/root/' + path
            if path in self.skipArry:
                continue
            self.fullpathArry.append(fullpath)
        print('目录获取完毕:', self.fullpathArry)

    # 上传Index文件
    def uploadIndex(self, sftp):
        for fullpathitem in self.fullpathArry:
            remoteIndex = fullpathitem + '/index.html'
            print('开始上传:' + remoteIndex)
            try:
                sftp.put(self.currentIndex, remoteIndex)
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
    host = '47.105.49.199'
    port = 22
    username = 'root'
    password = 'Aliyun1993*lwS'
    Server_code_update = Server_code_update(host, port, username, password)
    sftp, s = Server_code_update.connect_server()
    Server_code_update.getDirectory(sftp)
    Server_code_update.uploadIndex(sftp)
    s.close()
# **********002