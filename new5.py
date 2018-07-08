def get_res(branch,**subs):
	total = 0;
	for k,v in subs.items():
		if branch == 'cse' and k in ['c','java']:
			total+=v
	return total
sub = {'c':24,'java':30}
result = get_res('cse',**sub)
print result