#provides analysis on DNA sequences

def ATGC_content(DNA):  #returns ATGC contents in the form of a dict

    ATGCDict = {'A' : 0,
                'T' : 0,
                'G' : 0,
                'C' : 0}
    
    for nucleotide in DNA:
        if nucleotide == 'A':
            ATGCDict['A'] += 1
        elif nucleotide == 'T':
            ATGCDict['T'] += 1
        elif nucleotide == 'G':
            ATGCDict['G'] += 1
        else:
            ATGCDict['C'] += 1
            
    return ATGCDict


def complementary(DNA): #todo: given a DNA sequence, will return a complementary DNA sequence
    
    cDNA=[]
    
    for nucleotide in DNA:
        if nucleotide == 'A':
            cDNA.append('T')
        elif nucleotide == 'T':
            cDNA.append('A')
        elif nucleotide == 'G':
            cDNA.append('C')
        elif nucleotide == 'C':
            cDNA.append('G')
        else:
            cDNA.append('X') #Unknown base
    
    return cDNA


def hamming_differences(DNA1,DNA2): #todo: Returns info on positional/nucleotide differences in 2 DNA strands
    hDiff = []
    if len(DNA1)>len(DNA2):
        for i in range(len(DNA1)):
            DNA2+='X'
    else:
        for i in range(len(DNA2)):
            DNA1+='X'
    for n1,n2 in list(zip(DNA1,DNA2)):
        if n1!=n2:
            locDiff = list(zip(DNA1, DNA2)).index((n1, n2))
            nucDiff = n1+n2
            print(str(locDiff)+nucDiff)
            hDiff.append(str(locDiff)+nucDiff)
    return hDiff