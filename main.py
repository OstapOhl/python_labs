import zipfile
import re


def zip_open(path):

	with zipfile.ZipFile( path + ".zip" , "r" ) as zip_ref:
		zip_ref.extract("unzipped", path="")

		print("zip file unzipped\n")
		print("\n\n\n")
		zip_ref.printdir()
		print("\n")

	return "unzipped"


def zip_regex(path):

	pattern = re.compile("\D*http\D*sportszone\D*gif\D*")
	counter = 0
	textfile = open(path, 'r')
	filetext = textfile.read()
	textfile.close()

	for match in re.finditer(pattern, filetext):
		print ("Found: %s" % ( match.group()) + "\n")
		counter = counter + 1
	print("Matches found:")
	print(counter)



zip_regex(zip_open("zip"))