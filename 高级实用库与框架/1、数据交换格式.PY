#主要介绍CSV、XML、JSON和配置文件四种数据交换格式
#其中重点是XML和JSON

#1、CSV
#CSV是逗号分隔值（Comma-Separated Values）的简称，是电子表格和数据库最常用的数据交换格式
#CSV是一种简单的文件格式，以纯文本形式存储表格数据（数字和文本）
#python提供了csv模块来处理CSV文件
#csv模块的reader()函数可以读取CSV文件，返回一个迭代器
#csv模块的writer()函数可以写入CSV文件

#2、XML
#XML是可扩展标记语言（eXtensible Markup Language）的简称，用于传输和存储数据
#XML是一种树状结构的数据格式，由节点和属性组成
#XML的语法规则比较严格，必须严格遵守
#python提供了xml.etree.ElementTree模块来处理XML文件
#xml.etree.ElementTree模块的parse()函数可以解析XML文件，返回一个ElementTree对象
#Elementtree也有find()、findall()、iter()、iterfind()、itertext()等方法来查找XML文件中的节点和属性
#而XPATH是一种路径语言，用于在XML文档中查找节点和属性，XPath表达式可以作为查找的条件

#3、JSON
#JSON是JavaScript Object Notation的简称，是一种轻量级的数据交换格式
#JSON文档结构有两种：对象和数组
#对象是一个无序的“‘名称/值’对”集合，一个对象以“{”（左括号）开始，“}”（右括号）结束，每个“名称”后跟一个“:”（冒号）；“‘名称/值’对”之间使用“,”（逗号）分隔
#数组是一个值的有序集合，一个数组以“[”（左中括号）开始，“]”（右中括号）结束，值之间使用“,”（逗号）分隔
#python提供了json模块来处理JSON文件
#json模块的loads()函数可以将JSON字符串转换为Python对象
#json模块的dumps()函数可以将Python对象转换为JSON字符串
#json模块的load()函数可以从文件中读取JSON数据，返回一个Python对象
#json模块的dump()函数可以将Python对象写入文件
#JSON数据和Python对象之间的转换关系如下：
#JSON数据	Python对象
#{}		dict
#[]		list
#"string"	str
#1234.56	int或float
#true/false	True/False
#null		None

#4、配置文件
#配置文件是一种存储配置信息的文件，通常用于存储程序的配置参数
#配置文件的格式可以是ini、xml、json等
#配置文件的优点是可以方便地修改配置参数，而不需要修改程序代码
#python提供了configparser模块来处理ini格式的配置文件
#configparser模块的ConfigParser()函数可以读取ini格式的配置文件，返回一个ConfigParser对象
#ConfigParser对象的sections()方法可以获取所有的节点
