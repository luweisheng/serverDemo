import os
# 一、上传到代码服务器
#  1、进入git目录： git add .
#  2、git commit -m "更新说明"
#  3、git push
# 二、同步到应用服务器
#  1、进入应用服务器的git目录： git fetch origin master
#   提示输入用户名密码
#  2、git merge master origin/master
git_path = 'D:\\odoo\\serverDemo\\'
# 切换路径，进入项目路径
os.chdir(git_path)

# 获取当前路径的文件以及文件夹
all_file = os.listdir(git_path)
# print(all_file)

def git_operation():
    # 将代码添加到暂存区
    os.system('git add .')
    # 将代码提交到本地仓库
    os.system('git commit -m "版本号002"')
    # 将本地仓库推送到远程仓库：git@github.com:luweisheng/serverDemo.git
    os.system('git push https://git@github.com/luweisheng/serverDemo.git master')
    print('成功将本地项目推送到远程仓库')
if '.git' in all_file:
    git_operation()
else:
    # init初始化 git 仓库
    os.system('git init')
    git_operation()
# **********002