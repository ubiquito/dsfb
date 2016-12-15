import os
import os.path
from django.conf import settings

START_PATH = settings.BASE_DIR



class FileException(Exception):
	""" Exception subclass for filesystem related exceptions """
	def __init__(self, msg):
		Exception.__init__(self)
		self.msg = msg

def check_validpath(path):
	pass
	
	
def check_dir(path):
	
	if not os.path.isdir(path):
		raise FileException('Sorry, "' + path + '" must be a directory.')

	
def check_exists(path):

	if not  os.path.exists(path):
		raise FileException('Sorry, "' + path + '" does not exist.')


def os_walk( path ):

	"""
	Walk first level of a filesystem path.

	Returns a tuple of `pwd`, list of directories, list of files.  
	( pwd, [dir,dir2,...], [file,file2,...] )
	"""
	
	# clean input	
	path = os.path.normcase(path)

	check_validpath(path)
	check_exists(path)
	check_dir(path)


	# Include directory above (..)	
	dirs = [ '..' ]
	files = []
	
	# get curdir contents
	for (dirpath, dirnames, filenames) in os.walk(path):
		dirnames.sort()
		filenames.sort()
		dirs += dirnames
		files += filenames
		break

	pwd = path
	r = (pwd, dirs, files)
	return r



def walk_format( in_path ):

	"""
	Given a path...do os.walk, returns a dict.
	If no path, start at START_PATH 
	{
		'pwd':'/blah/foo', 
		'dirs':[
			{'dname':'done','dpath':'/blah/foo/done'},
			{'dname':'dtwo','dpath':'/blah/foo/dtwo'}
			],
		'files':[
			{'fname':'spam'},
			{'fname':'eggs'}
		]
	}		
	"""

	# Validate input
	in_path = in_path.strip()
	if len(in_path) == 0:
		in_path = START_PATH

	in_path = os.path.normpath(in_path)
	in_path = os.path.abspath(in_path)

	
	os_path = in_path

	# Walk
	(os_pwd, rel_dirs, rel_files) = os_walk(os_path)

	# Format
	out_pwd =  in_path
	result = {'pwd': out_pwd, 'dirs':[], 'files':[]}
	
	for rd in rel_dirs:
		dname = rd
		dpath = os.path.join( out_pwd, rd )
		dformat = { 'dname':dname, 'dpath':dpath }
		result['dirs'].append( dformat )

	for rf in rel_files:
		fname = rf
		result['files'].append( fname )

	return result
	
