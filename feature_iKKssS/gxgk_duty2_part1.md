# 任 务 二
这次的任务是使用 `Markdown` 语法记录 Git 的一些基础操作:从安装到仓库文件操作
***
## Git 安装：
我是在Windows上安装的，直接在Git官网直接 [下载安装程序](https://git-scm.com/downloads)，如果网速慢的话可以下载 [国内镜像](https://pan.baidu.com/s/1kU5OCOB#list/path=%2Fpub%2Fgit)，然后按默认选项安装即可。  
***
## Git的基础操作：
在此之前我是没有学习过Markdown的语法使用的，所以这次使用Markdown记录也是让我学习到了新的知识。  
写这篇记录之前，我是通过 [廖雪峰官网](https://www.liaoxuefeng.com/) 的文章来学习Git的基本操作的。这篇记录也是结合了 廖雪峰 所写的关于Git操作的文章来写的。  
   
### 1.创建版本库：
首先，选择一个合适的地方，创建一个空目录，我选择在了D盘创建一个名为 `gxgl_repository` 的空目录：

    $ cd d:
    $ mkdir gxgk_repository
    $ cd gxgk_repository
    $ pwd
    d:/gxgk_repository

这样我们就在D盘创建了一个名为 gxgk_repository 的空目录。用命令 `pwd` 可以查看当前所在位置。  
<font color=FF000 size=2 face="黑体">如果你使用Windows系统，为了避免遇到各种莫名其妙的问题，请确保目录名（包括父目录）不包含中文。</font>
  
  第二步：使用命令 `git init` 把这个目录编程 Git 可以管理的仓库：

    $ git init
    Initailized empty Git repository in d:/gxgk_repository

出现这样的提示就表示成功了。

 * 添加文件 ：  

    第一步，使用命令 `git add` 告诉 Git ，把文件提交到仓库

        $ git add xxx.xx

    `xxx.xx` 是指文件名（包括后缀）,输入完成后如果没有任何提示就表示添加成功了。~~廖雪峰大佬说Uinx的哲学就是没有消息就是好消息~~
      
    第二步：使用命令 `git commit` 告诉 Git，把文件提交到仓库：

        $ git commit -m "wrote a readme file"
        [master (root-commit) eaadf4e] wrote a readme file
        1 file changed, 2 insertions(+)
        create mode 100644 xxx.xxx

    `1 file changed` 表示有一个文件有改动， `2 insetions(+)` 表示增加了两行内容。`-m` 后面输入的是本次提交的说明。
    >`commit` 可以一次提交很多文件，所以你可以多次 `add` 不同的文件

    <font color=FF0000 size=2 face="黑体">后面的命令展现就步展现提示部分，仅展现代码部分了。具体可以看</font>[廖雪峰的 Git 教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)    
      
### 其余代码：
* 查看结果: `git status`  
git status  命令可以让我们时刻掌握仓库的当前状态。
* 查看不同：`git diff`
可以了解对仓库内文件作了什么修改。  
* 查看文件各版本：`git log`
查看每次修改提交的文件版本  
<font color=ff0000 size=2 face="黑体">如果输出信息太多的话可以加上 `--pretty=online`</font>  
* 版本回溯：`git reset --hard commit_id`  
回到指定 commit_id 的版本
>### 工作区和暂存区:
> 
> 在我们的电脑里能看到的目录，比如我创建的 gxgk_repository 文件夹就是一个工作区。  
在工作区有一个隐藏目录 `.git`，这个不算工作区，而是 Git 的版本库。Git 的版本库里存了很多东西，其中重要的就是称为 stage（或者叫index）的暂存区，还有 Git 为我们自动创建的第一个分支 `master` ,以及只想 `mastser`的一个指针叫 `HEAD`。  
添加文件的工作原理：`git add` 将要提交的所有修改放到暂存区（Stage），然后，执行 `git commit` 就可以一次性把暂存区的所有修改提交到分支。  
* 丢弃工作区的修改：`git checkout -- file`
* 丢弃暂存区的修改：`git reset HEAD <file>`
* 删除文件：`git rm file`
文件要包括文件后缀
>特殊情况：
如果你在文件管理器 `rm` 讲文件删除了，Git 知道你删除了文件，工作区和版本库就不一致了，用 `git status` 命令会告诉你哪些文件本删除了。然后你可以用 `git rm file` 删除，并且 `git commit`。也可以 `git checkout -- file` 把删除文件恢复到最新版本.  
## 总结：
总的来说，刚开始学习Git操作还是很简单的，对于 Git 的工作区和暂存区的工作原理的理解 是到目前为止学习Git的使用相对来说~~其实也挺简单的~~比较难的一个地方。继续努力！加油，<font color=ff0000 size=3 face="黑体">for myself !</font>
    