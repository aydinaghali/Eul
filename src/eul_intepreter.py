from sys import argv
from ctypes import c_ulong as u32

def eul(code):
	env = []
	try:
		debug = code[0] == ';'
	except IndexError:
		debug = False
	for j in input('> '):
		env.insert(0, u32(ord(j)))
	labels = []
	y = 0
	while y < len(code):
		if code[y] == '$':
			labels.append(y)
		y += 1
	in_str = False
	in_num = False
	num = ''
	i = 0
	if debug:
		i = 1
	while i < len(code):
		t = code[i]
		try:
			if   t == '~':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('~')))
				else:
					env.pop(0)
			elif t == '[':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('[')))
				else:
					a = env[len(env)-1]
					env.pop(len(env)-1)
					env.insert(0, a)
			elif t == ']':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord(']')))
				else:
					a = env[0]
					env.pop(0)
					env.append(a)
			elif t == '+':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('+')))
				else:
					a = env[0].value
					b = env[1].value
					env.pop(0)
					env[0] = u32(b+a)
			elif t == '-':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('-')))
				else:
					a = env[0].value
					b = env[1].value
					env.pop(0)
					env[0] = u32(b-a)
			elif t == '*':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('*')))
				else:
					a = env[0].value
					b = env[1].value
					env.pop(0)
					env[0] = u32(b*a)
			elif t == '/':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('/')))
				else:
					a = env[0].value
					b = env[1].value
					env.pop(0)
					env[0] = u32(b//a)
			elif t == '>':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('>')))
				else:
					a = env[0].value
					b = env[1].value
					env.pop(0)
					env[0] = u32(b>a)
			elif t == '<':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('<')))
				else:
					a = env[0].value
					b = env[1].value
					env.pop(0)
					env[0] = u32(b<a)
			elif t == '=':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('=')))
				else:
					a = env[0].value
					b = env[1].value
					env.pop(0)
					env[0] = u32(b==a)
			elif t == '%':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('%')))
				else:
					a = env[0].value
					b = env[1].value
					env[0] = u32(b%a)
			elif t == '&':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
				num = ''
				if in_str:
					env.insert(0,u32(ord('&')))
				else:
					a = env[0].value
					b = env[1].value
					env.pop(0)
					env[0] = u32(b and a)
			elif t == '|':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('|')))
				else:
					a = env[0].value
					b = env[1].value
					env.pop(0)
					env[0] = u32(b or a)
			elif t == '?':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('?')))
				else:
					if env[1].value:
						i = labels[env[0].value]
					env.pop(0)
			elif t == '!':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('!')))
				else:
					env[0] = u32(not env[0].value)
			elif t == '#':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('$')))
				else:
					a = env[0].value
					env.pop(0)
					for p in str(a):
						env.insert(0,u32(ord(p)))
			elif t == '@':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('@')))
				else:
					a = env[0].value
					res = 0
					while a:
						res += int(chr(env[a].value))*(10**(a-1))
						env.pop(a)
						a -= 1
					env[0] = u32(res)
			elif t == '\\':
				if   code[i+1] == '\'':
					if in_num:
						in_num = False
						env.insert(0,u32(int(num)))
						num = ''
					env.insert(0,u32(ord('\'')))
					in_str = True
					i += 1
				elif code[i+1] == '\\':
					if in_num:
						in_num = False
						env.insert(0,u32(int(num)))
						num = ''
					env.insert(0,u32(ord('\\')))
					in_str = True
					i += 1
				elif code[i+1] == '\n':
					if in_num:
						in_num = False
						env.insert(0,u32(int(num)))
						num = ''
					env.insert(0,u32(ord('\n')))
					in_str = True
					i += 1
			elif t == "'":
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				in_str = not in_str
			elif t in ['0','1','2','3','4','5','6','7','8','9']:
				if in_str:
					env.insert(0,u32(ord(str(t))))
				else:
					in_num = True
					num = num+t
			elif t == '.':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
			elif t == '$':
				pass
			elif t == '\n':
				pass
			elif t == ':':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord(':')))
				else:
					env.insert(0,env[0])
			elif t == '_':
				if in_num:
					in_num = False
					env.insert(0,u32(int(num)))
					num = ''
				if in_str:
					env.insert(0,u32(ord('_')))
				else:
					env[0], env[1] = env[1], env[0]
			else:
				in_str = True
				env.insert(0,u32(ord(t)))
		except Exception as e:
			print(e, '@', i)
		i += 1
		if debug:
			print(list(map(lambda x:x.value,env)))
	if in_num:
		env.insert(0,u32(int(num)))
	if debug:
		print(list(map(lambda x:x.value,env)))
	env.reverse()
	for k in env:
		print(chr(k.value), end='')

eul(open(argv[1], 'r').read())
