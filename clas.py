# import re
# with open('ax','r',encoding='utf-8') as f1:
#     l = []
#     for i in f1:
#         ret=re.findall('1[3-9]\d{9}', i)
#         ret1=re.match('1[3-9]\d{9}', i)
#         l.extend(ret)
# print(l)
# print(ret1.group())
# import re
# ret=re.findall('l','luhan,lll,akakl')
# print(ret)
#['l', 'l', 'l', 'l', 'l']
# findall接收两个参数 ： 正则表达式 要匹配的字符串
# 一个列表数据类型的返回值：所有和这条正则匹配的结果
# import re
# ret=re.findall('\d+','92lwljsie9292')
# print(ret)
#['92', '9292']
#re.findall()有关的例子：查找一个文件夹里边的电话号
# with open('ax','r',encoding='utf-8') as f:
#     l=[]
#     for i in f:
#         ret=re.findall('1[3-9]\d{9}',i)
#         l.extend(ret)
# print(l)
#['17839948653', '16601162643', '18929283939']
# import re
# ret=re.search('uuuu','usuuslsluuuu')
# print(ret)
# #<_sre.SRE_Match object; span=(0, 1), match='u'>
# # 如果匹配到了，返回一个结果对象
# # 如果没匹配到，返回一个None
# if ret:
#     print(ret.group())   #uuuu   r如果没有则返回的是None
#  # 从结果对象中获取结果
# import re
# ret=re.match('al','alalalallajdjjdjd')
# if ret:
#     print(ret.group())   #al
# import re
# ret=re.subn('\d','H','kslsi29jjd')
# print(ret)
# #('kslsiHHjjd', 2)
# # #将数字替换成'H'，返回元组(替换的结果,替换了多少次)
# import re
# obj=re.compile('\d+')  # 编译 在多次执行同一条正则规则的时候才适用
# ret1=obj.findall('282jks92111jdj')
# ret2=obj.search('jajaj9292ksnnvdl2')
# print(ret2.group())
# print(ret1)
# # 9292
# # ['282', '92111']
# import re
# ret=re.finditer('\d','jd8sk3sks3222s')#finditer适用于结果比较多的情况下，能够有效的节省内存
# print(ret)#<callable_iterator object at 0x000001B5BA5BE7B8>
# # print(ret.__next__().group())  #8
# # for i in ret:
# #     print(i.group())  #8
# print(next(ret).group())  #查看第一个结果
# print(next(ret).group())  #查看第二个结果
# print([i.group() for i in ret])  #查看剩余的左右结果
# # 8
# # 3
# # ['3', '2', '2', '2']
# # 当分组遇到re模块
# import re
# ret1 = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
# ret2 = re.findall('www.(?:baidu|oldboy).com', 'www.baidu.com')
# print(ret1)
# print(ret2)
# # ['oldboy']
# # ['www.baidu.com']
# # findall会优先显示组内匹配到的内容，如果想取消分组优先效果，在组内开始的时候加上?:
# import re
# ret=re.split("\d+","eva3egon4yuan")
# print(ret) #结果 ： ['eva', 'egon', 'yuan']
# ret=re.split("(\d+)","eva162784673egon44yuan")
# print(ret) #结果 ： ['eva', '162784673', 'egon', '44', 'yuan']
# # split分割一个字符串，默认被匹配到的分隔符不会出现在结果列表中，
# # 如果将匹配的正则放到组内，就会将分隔符放到结果列表里
# "<h1>hello</h1>"
# import re
# ret = re.findall('<\w+>(\w+)</\w+>',"<h1>hello</h1>")
# print(ret)  #['hello']
# 分组命名
import re
ret = re.search("<(?P<tag>\w+)>(?P<content>\w+)</(?P=tag)>","<h1>hello</h1>")
print(ret)
print(ret.group())   # search中没有分组优先的概念<h1>hello</h1>
print(ret.group('tag'))#h1
print(ret.group('content'))#hello
ret = re.search(r"<(\w+)>(\w+)</\1>", "<h1>hello</h1>")
#如果不给组起名字，也可以用\序号来找到对应的组，表示要找的内容和前面的组内容一致
# #获取的匹配结果可以直接用group(序号)拿到对应的值
print(ret.group())
print(ret.group(0))  #结果 ：<h1>hello</h1>
print(ret.group(1))  #结果 ：h1
print(ret.group(2))  #结果 ：hello
