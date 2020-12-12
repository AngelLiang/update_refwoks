# coding=utf-8
"""
## 脚本说明

修复知网导出 Refworks 格式字段与 zotero 不匹配问题

替换算法规则说明，文本每行按顺序替换以下单词

- `PP `     ->  `VO `
- `AD `     ->  `LL `
- `PB `     ->  `JO `
- `/Thesis` ->  ``        （即删掉）
- `SR 1`    ->  ``        （即删掉）
- `DS CNKI` ->  `SL CNKI`
- `A3 `     ->  `PP `


## 准备工作

- 安装Python3


## 使用方式

1、把脚本和Refworks文件放在同一个目录下
2、在命令行窗口（cmd或PowerShell）输入 `python3 update_refwoks.py "<文件路径>"` （可以使用[tab]键完成自动输入）
3、回车完成，之后会在当前目录下出现一个 `<文件名>（改）` 的新文件，这个就是修改过的文件。


## 备注

- 暂时只能一次替换一个文件，即如果需要替换多个文件，需要多次输入命令，例如：

    python3 update_refwoks.py "<文件路径1>"
    python3 update_refwoks.py "<文件路径2>"
    python3 update_refwoks.py "<文件路径3>"

"""

import os
import sys
import shutil

document = sys.argv[1]

# 拷贝文件
# 文件名.txt -> 文件名（改）.txt
name, ext = os.path.splitext(document)
new_document = name+'（改）' + ext
shutil.copy(document, new_document)

content = ''

with open(new_document, mode='r', encoding='utf-8') as fp:
    # 替换字符
    for line in fp:
        # Journal文献
        # line = line.replace('SR 1', '' , 1)             # 后面会替换
        # line = line.replace('DS CNKI', 'SL CNKI')   # 后面会替换
        line = line.replace('PP ', 'VO ', 1)  # 加空格是为了避免 APP 等单词被替换为 AVO
        line = line.replace('AD ', 'LL ', 1)
        line = line.replace('PB ', 'JO ', 1)

        # 硕博论文
        line = line.replace('/Thesis', '', 1)
        line = line.replace('SR 1', '', 1)
        line = line.replace('DS CNKI', 'SL CNKI', 1)
        line = line.replace('A3 ', 'PP ', 1)
        content += line

with open(new_document, mode='w', encoding='utf-8') as fp:
    # 写入新文件
    fp.write(content)
