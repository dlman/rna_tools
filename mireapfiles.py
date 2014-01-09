"""
This script takes in a sam file and outputs files for use with Mireap. 
Note: Unaligned reads in sam file will be skipped.
"""

def main():
	# note: this script will skip unaligned reads (in sam if 3rd column has *)
	import argparse

	parser = argparse.ArgumentParser(description="Takes sam file and outputs\
		files for Mireap")
	parser.add_argument("sam", help="sam input file")
	parser.add_argument("o", help="the output prefix")

	args = parser.parse_args()

	with open(args.sam) as sam, open(args.o + "_in.fa"
		, "w") as fa_output, open(args.o + "_map.txt", "w") as map_output:
		for line in sam:
			# skip headers
			if line[0] == '@':
				continue
			else:
				splitter = line.split()
				id_ = splitter[0]
				# 0 is + strand, 16 is -
				if splitter[1] == "0":
					sense = "+"
				else:
					sense = "-"
				ref = splitter[2]
				start = int(splitter[3])
				end = start + len(splitter[9]) - 1
				# output info to files for mireap input
				map_output.write("{}\t{}\t{}\t{}\t{}\n".format(id_,
						ref,str(start),str(end),sense))
				fa_output.write(">{}\n{}\n".format(
					id_,splitter[9]))

if __name__ == "__main__":
	main()