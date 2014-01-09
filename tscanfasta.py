import argparse

parser = argparse.ArgumentParser(description="Takes sam file and outputs\
	sequences in fasta format")
parser.add_argument("-i", help="sam input file")
parser.add_argument("-l", nargs=2, help="")
parser.add_argument("-o", help="the output file")
args = parser.parse_args()

with open(args.i) as sam, open(args.o, "w") as output:
	for line in sam:
		# skip headers
		if line[0] == '@':
			continue
		else:
			splitter = line.split()
			id_ = splitter[0]
			seq = splitter[9]
			# if -l is set, only take sequences between the set min/max nt
			if args.l:
				if int(args.l[1]) >= len(seq) >= int(args.l[0]):
					 output.write('>' + id_ + '\n' + seq + '\n')
			# otherwise take all sequences
			else:
				output.write('>' + id_ + '\n' + seq + '\n')