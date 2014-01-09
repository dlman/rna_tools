"""
Transforms a sam file into a fasta file with optional min
and max nt length. Note: unaligned reads in sam file will be skipped.
"""

def main():
	# note: this script will skip unaligned reads (in sam if 3rd column has *)
	import argparse

	parser = argparse.ArgumentParser(description="Takes sam file and outputs\
		sequences in fasta format")
	parser.add_argument("sam", help="sam input file")
	parser.add_argument("o", help="the output file")
	parser.add_argument("-l", nargs=2, help="minimum and maximum nt length")

	args = parser.parse_args()


	with open(args.sam) as sam, open(args.o, "w") as output:
		for line in sam:
			# skip headers
			if line[0] == '@':
				continue
			else:
				splitter = line.split()
				# if not an unaligned read
				if splitter[2] != '*':
					id_ = splitter[0]
					seq = splitter[9]
					# if -l is set, only take sequences between the set min/max nt
					if args.l:
						if int(args.l[1]) >= len(seq) >= int(args.l[0]):
							 output.write('>{}\n{}\n'.format(id_, seq))
					# otherwise take all sequences
					else:
						output.write('>' + id_ + '\n' + seq + '\n')

if __name__ == "__main__":
	main()