#!/usr/bin/env python3

import re

class LayeredMapping:
	def __init__(self, *layers):
		assert len(layers) > 0
		self.layers = layers
	def __getitem__(self, key):
		for layer in self.layers:
			try:
				return layer[key]
			except KeyError:
				continue
		else:
			raise KeyError(key)

class MacroLib:
	def __init__(self, source=None):
		self.defs = {}
		self.vals = {}
		if source:
			self.parse(source)

	defpat = re.compile(r'^#\s*define\s+(\w+(?:\([^)]*\))?)\s+(.*[^\s])?\s*$')
	funcpat = re.compile(r'^(\w+)\(([^)]*)\)$')
	def parse(self, source):
		for line in source:
			m = self.defpat.match(line)
			if not m:
				print(f"Skipping {line!r}")
				continue
			name, value = m.groups()
			if name in self.defs: print(f"WARNING: redefinition of {name}")
			func = self.funcpat.match(name)
			if func:
				name, args = func.groups()
			if not value:
				self.vals[name] = True
				continue
			value = self.cleandef(value)
			if func and args:
				value = self.makefunc(name, args, value)
			self.defs[name] = value

	notpat = re.compile(r'!(?!=)')
	@classmethod
	def cleandef(cls, value):
		return cls.notpat.sub(' not ', value.replace('&&', ' and ').replace('||', ' or '))

	def makefunc(self, fname, arglist, value):
		#print(f"Making {fname}: {arglist} = {value}")
		argnames = tuple(s.strip() for s in arglist.split(','))
		def func(*args):
			params = dict(zip(argnames, args))
			#print(f"Evaluating {fname} with {params}")
			return self.eval(value, params)
		anames = ','.join(argnames)
		func.__doc__ = f"{fname}({anames}) = {value}"
		return func

	def __getitem__(self, key):
		try:
			val = self.vals[key]
		except KeyError:
			rval = self.defs[key]
			if callable(rval):
				return rval
			self.vals[key] = None
			try:
				val = self.eval(rval)
			except (KeyError, ValueError, NameError, SyntaxError):
				return rval
			finally:
				del self.vals[key]
			self.vals[key] = val
		else:
			if val is None:
				raise RuntimeError(f"Recursion detected evaluating {key}")
		return val

	def eval(self, expr, params=None):
		return eval(expr, {}, LayeredMapping(params, self) if params else self)

def command_line(ml):
	try:
		expr = input('eval> ')
	except (EOFError, KeyboardInterrupt): return False
	if not expr: return True
	try:
		if expr.startswith('?'):
			expr = expr[1:]
			val = ml.defs[expr]
		else:
			val = ml.eval(expr)
	except KeyError:
		print(f"{expr} not defined")
	except Exception as e:
		print(f"Error evaluating {expr}: {e}")
	else:
		if callable(val) and val.__doc__:
			print(val.__doc__)
		else:
			print(f"{expr} = {val}")
	return True

if __name__ == '__main__':
	import fileinput, readline
	def main():
		ml = MacroLib(fileinput.input())
		while command_line(ml): pass
		print()

	main()

