with open("pseudo_mtRNA_combined.txt") as mtrna, open("pseudo_mtRNA_map", "w") as mtrna_map, open("pseudo_mtRNA_combined.fa","w") as fasta:
	next(mtrna)
	ref = "01_DZ01_Edited"
	for line in mtrna:
		splitter = line.split()
		id_ = splitter[0]
		start = splitter[2]
		stop = splitter[3]
		sense = splitter[4]
		mtrna_map.write(id_ + "\t" + ref + "\t" + start + "\t" + stop + "\t" + sense + "\n")
		fasta.write(">" + id_ + "\n" + splitter[1] + "\n")