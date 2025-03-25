# 정규표현식 시작하기

# 문자 클래스 [] 
# [abc]
# [] 사이의 문자들과 매치
# "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
# "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
# "dude"는 정규식과 일치하는 문자인 a, b, c 중 어느 하나도 포함하고 있지 않으므로 매치되지 않음
# 하이픈을 사용하여 From-To로 표현 가능
# Ex) [a-c] = [abc], [0-5] = [012345]
# 

# Dot(.)
# a.b 
# 줄바꿈(\n)을 제외한 모든 문자와 매치
# "aab"는 가운데  "a"가 모든 문자를 의미하는 '.'과 일치하므로 정규식과 매치
# "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 '.'과 일치하므로 정규식과 매치
# "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는있어야 하는 이 정규식과 일치하지 않으므로 매치되지 않는다.
#  DOTALL, S
# import re
# # p = re.compile('a.b')
# # m = p.match('a\nb')
# # print(m)
# p = re.compile('a.b', re. S)
# m = p.match('a\nb')
# print(m)



# 반복(*)
# ca*t
# "ct"는 "a"가 0번 반복되어 매치
# "cat"는 "a"가 0번 이상 반복되어 매치 (1번 반복)
# "caaat"는 "a"가 0번 이상 반복되어 매치 (3번 반복)
# 
# 반복(+)
# # "ct"는 "a"가 0번 반복되어 매치
# "cat"는 "a"가 1번 이상 반복되어 매치 (1번 반복)
# "caaat"는 "a"가 1번 이상 반복되어 매치 (3번 반복)
# 
# 반복({m,n},?)
# ca{2}t
# "cat"는 "a"가 1번만 반복되어 매치되지 않음
# "caat"는 "a"가 2번 반복되어 매치
# 
# 반복({m,n},)
# ca{2,5}t
# "cat"는 "a"가 1번만 반복되어 매치되지 않음
# "caat"는 "a"가 2번 반복되어 매치
# "caaaaat"는 "a"가 5번 반복되어 매치
# 
# 반복({m,n},?)
# ab?c
# "abc"는 "b"가 1번 사용되어 매치
#  "ac"는 "b"가 0번 사용되어 매치
# ? == {0,1}와 같은 표현

# import re
# p = re.compile('[a-z]+')
# m = p.match('python')
# print(m)

# import re
# p = re.compile('[a-z]+')
# m = p.search('3 python')
# print(m)

# import re
# p = re.compile('[a-z]+')
# m = p.findall('life is too short')
# print(m)

# import re
# p = re.compile('[a-z]+')
# m = p.finditer('life is too short')
# print(m)

# match 객체 메서드
# import re
# p = re.compile('[a-z]+')
# m = p.match('python')
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())

# # IGNORECASE, I
# import re
# p = re.compile('[a-z]')
# print(p.match('python'))
# print(p.match('python'))
# print(p.match('python'))

# MULTILINE, M
# import re
# p = re.compile("^python\s\w+",re. M)

# data = """python one
# life is too short
# python two
# you need python
# python three"""

# print(p.findall(data))

# VERBOSE, X
# import re
# charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

# charref = re.compile(r"""
#  &[#]               Start of a numeric entity reference
#  (
#      0[0-7]+        Octal form
#    | [0-9]+         Decimal form
#    | x[0-9a-fA-F]+  Hexadecimal form
#  )            
#  ;                  Trailing semicolon
# """, re.VERBOSE)

# 백슬래시 문제
# \section x
# p = re.compile('\\section')
# p = re.compile('\\\\section')
# p = re.compile(r'\\section')

# 메타문자 |
# import re
# p = re.compile('Crow|Servo')
# m = p.match('CrowHello')
# print(m)

# 메타문자 ^
# import re
# print(re. search('^Life', 'Life is too short'))
# print(re. search('^Life', 'My Life'))

# 메타문자 $
# import re
# print(re.search('short$', 'Life is too short'))
# print(re.search('short$', 'Life is too short, you need python'))

# 메타문자 \b
# import re
# p = re.compile(r'\bclass\b')
# print(p.search('no class at all'))
# print(p.search('the declassified algorithm'))
# print(p.search('one subclass is'))

# 그루핑 ()
# import re
# p = re.compile('(ABC)+')
# m = p.search('ABCABCABC OK?')
# print(m)
# print(m.group())

# 그루핑2 ()
# import re
# p = re.compile(r"(\w+)\s+\d+[-]\d\[-]\d+")
# m = p.search("park 010-1234-1234")
# print(m.group(1))

# 그루핑 ()
# import re
# p = re.compile(r'(\b\w+)\s+\1')
# print(p.search('Paris in the the spring'.group()))

# 그루핑된 문자열에 이름 붙이기 ? P<name>
# import re
# p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
# m = p.search("park 010-1234-1234")
# print(m.group("name"))

# 전방탐색: 긍정형 (?=)
# import re
# p = re.compile(".+(?=:)")
# m = p.search("http://google.com")
# print(m.group())

# 전방탐색: 부정형 (?!)
# import re
# p = re.compile(".*[.](?!bat$)."$", re.M")
# l = p.findall("""
# autoexec.exe
# autoexec.Bat
# autoexec.jpg
# """)
# print(l)

# # 문자열 바꾸기 sub
# import re
# p = re.compile('(blue|white|red)')
# p.sub('colour', 'blue socks nad red shoed')

# Greedy vs Non-Greedy
# import re
# s = '<html><head><title>Title</title>'
# print(re.match('<.*>', s).group*())
# print(re.match('<.*?>', s).group*())