# google_scholar_references
## 项目目的
使用scrapy框架爬取经谷歌学术搜索关键词后排名第一的参考文献格式，快速生成标准参考文献
## 安装要求
scrapy 翻墙请务必开全局模式不用PAC模式（shadowsocks）
## 项目运行
将要搜索的关键词或者引用文章名称逐行保存在paper.txt中，运行run.py，标准的GB/T 7714格式参考文献自动保存在paper_references.txt中（默认导入的是被引次数最高的文献）
