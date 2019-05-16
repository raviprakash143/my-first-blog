if 5>2:
	print('test')
list = ['hyd','bza','gnt']
print('List: ',list)
for t in list:
	print(t)
if "bza" in list:
	print('Avaliable "bza" in List:',list)
def tri_recursion(g):
	if(g>0):
		result=g+tri_recursion(g-1)
		print(result)
	else:
		result=0
	return result
print("\n\nRecursion Results:")
tri_recursion(6)