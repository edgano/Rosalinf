# we define the function, it will recive the string to codify
def hammingDistance(seq1,seq2):
	dist=0 
	for i in range (0,len(seq1)):
		if seq1[i]!=seq2[i] : dist= dist+1 
	return dist

seq1="CCAGCAAGCATCACGACTCGGCTGGTCCTAATGTCCAAGTCTACCATTGAATCTACTAAGCTGAGCATGTCGGTGGTCCAGAATGGCAACGACAGTCCTCAGCACATGCAACCGGAATCCGTTATGGCCGAGATTTTATCACTAGCTGACACGAGGGGTGCGAATATACAGGGGTGGGAATGCTTGGTGGGACTCGTATCGTAACGAACGTACATCAAAAGGAGACAGCGCCAAGTTTAAGGCTGGACGCCAGCTCACTAGACCGACTCGACACGTGCAGGCCTAGGGGGTGGTACACTTAATCAAGCAATTTCTAACTATCGGCTGTAGCTCACCCGGTATCTGGACTGGTGCGTCATCGCCCCGGGAAGCTATTAACATGGTCGACTATACGAGTGCAACTTTGTTCACAGAACCCGTGTCGCTTACCAACAAAGGCGTAGGCTGTTGATCTCGTTGGCTTGTGACAACGCGCAAATTCACCGACCCCTTATCGTTAACAACAAAGGTTTATCCACGCCGAGATTGCCGACTATGTATAGACTTTGCATGTGCGTAGCGACCACCCGCCAGCTTAGGGTTAGCAGGATACCGCCGCCAGATCGGGCGACTCTGCTGAGTGGTAGATATCTCGTGGTCACTGGTAGCTTGTCAGTTACCCCATGACATGAATTCTATAGGATTGAGTTGTCCTTACGCACCACGTCGATAGTGACCTACAGTTGTCCACCTACTTCTACTATTTTGCCATCCGGGGACATCCTCCACAACCAGTCGGCCCGCCCGCTTAGAATGCATTGTATCCGGGCAGCGCCGTCGTAAGTCGGGCTGGGGTACTTTAGTAGAGAAGGAGGAGGTCCGCACACGGGGCATCTAAGGGAGCTGTCGTTTTACAGTCCGATGTTTGCTTCACAGATAGTCGGGT"
seq2="TTCGCCCTAAACACATAGCGGTTCATCCTGTCATTCTTGTCCGTCGTTGATACGGCCCTAGTACTGATTGAAAGGTCCCATAATTGCCAAATCCGTCCGAAACGAAGGAAGTGGGACCCCGTTCCGGTCGGGAATTGATCAGGAGCGACGTGTAGAACTCCGTACTTGCAGCAGTGGGAATCACTCGTGGTACGTTCATTATATACTACTTAGCCCCGTACTAGGAGCCTGGGAGGTTACGACCCTCTAACAGCATAATAAGCCCAAACACCACGGCGACTCACAGTCGAAGCAAATTTTACGCCAGAAATTTCGGTATTTCGCTTTTAGCGCAGCCGGGAGGTGGCCGCTTTCGTAAGCGACGGACGGACCTTTCACGAAGGGCGACCCCGTGAGAACTATTTTGTCGGCATCATCGCTGTCGCAGATCCTTCATGCCGAGTCAAGTGGATTTGGCTGTGACTTCTGATCACTACACTTCAACGACGTCTTGACTTTATTATCAATGATTGATGCTCGCCGGTCTTTTAGACTGAATATTCAACCTGCAAGTCCTTAGTAACCATCGGCAGGCTGAACGGAATCTGGGTACTGCTCTGGTAACAGCTCGGTTATCATCATCGAAGACATCCGGAATCCTCAAGATGTTCGTGGGCTGCGCCGTGCCACACAAGCGCTTCGATTGTTGTTGACATACGGGAATTGACAATTGAACTCTATTAACGAGTGGGGACTCCGATGTGTTTAGAAGCTAGCGGGAACCTCGGTAGCTGGTGGGCCGTCCCACTTAGCATGTAGTGTAACCCGGCGACGCCGACAGTAGTATTGCTAAGTTACTTGGCTTGAATCAGGCGAGATTGTTATAAAGGGCATCCTGTTTACCAGTAGCTAAACACTCAAGGGATTGGGACCCAGATATACGGGC"

print hammingDistance(seq1,seq2)
