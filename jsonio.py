import simplejson
import json
from pprint import pprint

def put(data, filename):
	try:
		jsondata = simplejson.dumps(data, indent=4, skipkeys=True, sort_keys=True)
		fd = open(filename, 'w')
		fd.write(jsondata)
		fd.close()
	except:
		print 'ERROR writing', filename
		pass
 
def get(filename):
	get_data = None
	try:
		json_data = open(filename)
		get_data = json.load(json_data)
		json_data.close()
	except: 
		print 'COULD NOT LOAD:', filename
	return get_data