"""
This script takes in Sequery outputs and reconstructs a fastq file
with the unmatched fasta sequences that are found in the outputs.
"""
def main():
	import argparse

	parser = argparse.ArgumentParser(description="Reconstruct fastq file\
		with unmatched Sequery sequences")
	parser.add_argument('-i', nargs='*', help='Sequery output files')
	parser.add_argument('-f', nargs='*', help='original fastq file')
	parser.add_argument('-o', nargs=1, help='output fastq file')
	args = parser.parse_args()

	id_set = set([])

	if args.i and args.f and args.o:
		for item in args.i:
			start = False
			with open(item,'U') as currentfile:
				for line in currentfile:
					# skip blank lines
					if line.rstrip():
						# skip til unmatched section
						if line.find("were not matched") >= 0:
							start = True
							continue
						if start is True:
							if line.find(">") >= 0:
								id_ = line.rstrip()[1:]
								id_set.add(id_)

		with open(args.f[0]) as fastq, open(args.o[0],"w") as output:
			print_id = False
			for line in fastq:
				if line[0] == '@':
					test_id = line.rstrip()[1:]
					if test_id in id_set:
						print_id = True
					else:
						print_id = False
				if print_id is True:
					output.write(line)

if __name__ == "__main__":
	main()