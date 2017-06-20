import re
import sys

def find_head(line):
	p3 = r'<th.*?>(.*?)</th\s*>'
	contain_tr3 = re.findall(p3, line, re.DOTALL|re.IGNORECASE)
#	print(contain_tr3)
	return contain_tr3

def find_cell(line):
	p2 = r'<td.*?>(.*?)</td\s*>'
	contain_tr2 = re.findall(p2, line, re.DOTALL|re.IGNORECASE)
#	print(line)
#	print(contain_tr2)
	return contain_tr2


data = sys.stdin.read()
data = data.replace('\n','')
#print(data)

head_row = []
row = []
i = 1

p0 = r'<table.*?>(.+?)</table.*?>'
contain_tr0 = re.findall(p0, data, re.DOTALL|re.IGNORECASE)
#print(contain_tr0)
for content in contain_tr0:
	print('Table%d:'%i)
	i += 1
	p1 = r'<tr.*?>(.+?)</tr\s*>'
	contain_tr1 = re.findall(p1, content, re.DOTALL|re.IGNORECASE)
	#print(contain_tr1)

	for token in contain_tr1:
	#	print(token)
		head_row = find_head(token)
		row = head_row + find_cell(token)
	#	print(head_row)
	#	print(row)
	#	if head_row:
	#		print(re.sub('\s+',' ',','.join(head_row)))
	#		del head_row[:]
		if row:
			print(re.sub('\s+',' ',','.join(row)))
			del row[:]
	print('')







	







			
			
	
			


