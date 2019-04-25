import sys;

fileName = "";
if len(sys.argv) == 2:
	fileName = sys.argv[1];
else:
	print("please pass in a natepy file by running a command like 'python natepy.py Assignment2.npy'");
	exit();

def readFile():
	with open(fileName) as reader:
		return ';'.join(reader.read().split("\n"));

def main():
	'''.replace(" {", ":\n").replace("}", "*-*-")'''
	fileContents = [line.replace("\t", "").replace("    ", "") for line in readFile().split(";")];
	tabcount = 0;
	finalfile = "";
	for line in fileContents:
		offset = 0;
		line = line.replace("\n", "")
		if "++" in line:
			line = line.replace("++", " += 1");
		if "--" in line:
			line = line.replace("--", " -= 1");
		if "{" in line and "}" in line:
			print()
		elif "{" in line:
			line = line.replace(" {", ":");
			offset = 1;
		elif "}" in line:
			line = line.replace("}", "");
			offset = -1;
		if "else if" in line:
			line = line.replace("else if", "elif");
		if "//" in line:
			line = line.replace("//", "#");
		for i in range(tabcount):
			line = "\t" + line;
		finalfile += line + "\n";
		tabcount += offset;
	finalfile = "\n".join(list(filter(lambda x: x.strip() != '', finalfile.split("\n"))))
	finalfileName = fileName.replace(".npy", "_natepyoutput.py");
	with open(finalfileName, "w+") as writer:
		writer.write(finalfile + "\n");
	print ("you can now run the compiled output using the command 'python " + finalfileName + "'");

if __name__ == "__main__":
	main();
