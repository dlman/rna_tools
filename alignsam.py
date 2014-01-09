"""
This script takes in a sam file and gff file as inputs and finds the 
sequences in the sam that are within the gff sequences coordinates
given the user specified nt termini variation.
Outputs the non matches as well as matches. 
"""

def main():
	import argparse

	# arguments: sam file, nucleotide variation, gff file,
	# non matches output file, matches output file
	transcript_list = []
	parser = argparse.ArgumentParser(description="Test SAM file sequences for\
		matches against gff file sequences based on genome alignment.")
	parser.add_argument("sam", help="sam input file")
	parser.add_argument("nt", type=int, help="the nucleotide variation")
	parser.add_argument("gff", help="gff input file")
	parser.add_argument("non_output", help="ouput file for nonmatches")
	parser.add_argument("output", help="output file for matches")
	args = parser.parse_args()



	with open(args.sam) as sam, open(args.gff) as gff,\
	 open(args.non_output, "w") as none, open(args.output, "w") as output:
			for line in gff:
				splitter = line.split()
				# take in chr, name, start, end, strand
				info = splitter[0], splitter[1], int(splitter[3]),\
				 int(splitter[4]), splitter[6]
				transcript_list.append(info)
			for line in sam:
				matched = False
				# skip headers
				if line[0] == '@':
					continue
				splitter = line.split()
				name = splitter[0]
				chrom = splitter[2]
				start = int(splitter[3])
				seq = splitter[9]
				end = start + len(seq) - 1
				for item in transcript_list:
					# find matches with nt variations considered
					if chrom == item[0] and start >= (item[2] - args.nt) and \
					 end <= (item[3] + args.nt):
					 	matched = True
						output.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(chrom,
							str(start),str(end),name,seq,item[1],
							str(len(seq))))
				if matched is False:
					none.write("{}\t{}\t{}\t{}\t{}\n".format(chrom,
						 	str(start),str(end),name,seq))

if __name__ == "__main__":
	main()