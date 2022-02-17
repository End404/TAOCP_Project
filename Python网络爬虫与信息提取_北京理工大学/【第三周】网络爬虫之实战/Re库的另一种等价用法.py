
# ------- Re库的另一种等价用法 ------- #

import re 

# 函数式用法:一次性操作.
rst = re.search ( r'[1-9]\d{5}' , "BIT 100081" )
print ( rst )


# 面向对象用法：编译后的多次操作.
pat = re.compile( r'[1-9]\d{5}' )  # ?????
rs = pat.search( 'BIT 100081' )
print ( rs )


#**********************************************************************
'''
    regex = re.compile(pattern, flags=0) 将正则表达式的字符串形式编译成正则表达式对象.
    ∙ pattern : 正则表达式的字符串或原生字符串表示 .
    ∙ flags: 正则表达式使用时的控制标记.
'''
#***********************************************************************

# regex = re.compile(pattern, flags=0).
# 将正则表达式的字符串形式编译成正则表达式对象.
regex = re.compile(r'[1‐9]\d{5}')
print ( regex )



#------------------------------------------------------
'''
    ---另一种等价用法：
        regex.search()      在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
        regex.match()       从一个字符串的开始位置起匹配正则表达式，返回match对象
        regex.findall()     搜索字符串，以列表类型返回全部能匹配的子串 
        regex.split()       将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
     
        regex.finditer()    搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
        regex.sub()         在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串

'''
#-------------------------------------------------------



