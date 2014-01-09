# takes sequences from sam file, tests if they match in gff file ranges

import sys

transcript_list = []

if len(sys.argv) > 3:
	with open(sys.argv[1]) as sam:
		with open(sys.argv[2]) as gff:
			with open (sys.argv[3], "w") as output:
				for line in gff:
					splitter = line.split()
					# take in chr, name, start, end, strand
					info = splitter[0], splitter[1], int(splitter[3]), int(splitter[4]), splitter[6]
					transcript_list.append(info)
				for line in sam:
					if line[0] == '@':
						continue
					splitter = line.split()
					name = splitter[0]
					chrom = splitter[2]
					start = int(splitter[3])
					seq = splitter[9]
					end = start + len(seq)
					for item in transcript_list:
						if chrom == item[0] and start >= item[2] and end <= item[3]:
							output.write(chrom + "\t" + str(start) + "\t" + str(end) + "\t" + name + "\t" + seq + "\t" + item[1] + "\t"
							+ "\t" + str(len(seq)) + "\n")
