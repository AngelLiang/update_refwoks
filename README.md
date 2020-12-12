## 脚本说明

修复知网导出 Refworks 格式字段与 zotero 不匹配问题

替换算法规则说明，文本每行按顺序替换以下单词

- `PP` -> `VO`
- `AD` -> `LL`
- `PB` -> `JO`
- `/Thesis` -> `` （即删掉）
- `SR 1` -> `` （即删掉）
- `DS CNKI` -> `SL CNKI`
- `A3` -> `PP`

## 准备工作

- 安装 Python3

## 使用方式

1、把脚本和 Refworks 文件放在同一个目录下
2、在命令行窗口（cmd 或 PowerShell）输入 `python3 update_refwoks.py "<文件路径>"` （可以使用[tab]键完成自动输入）
3、回车完成，之后会在当前目录下出现一个 `<文件名>（改）` 的新文件，这个就是修改过的文件。

## 备注

- 暂时只能一次替换一个文件，即如果需要替换多个文件，需要多次输入命令，例如：

```
python3 update_refwoks.py "<文件路径 1>"
python3 update_refwoks.py "<文件路径 2>"
python3 update_refwoks.py "<文件路径 3>"
```
