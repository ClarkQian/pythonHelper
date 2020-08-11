import re
def sort_key(s):
	if s:
		try:
			#截取需要的部分
			c = re.findall('(\d+).pdf', s)[0]
		except:
			c = -1
		return int(c)


def strsort(alist):
    alist.sort(key=sort_key, reverse = True)
    return alist
