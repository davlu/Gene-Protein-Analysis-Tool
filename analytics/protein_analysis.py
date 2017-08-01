# Needed for regex
import re

# Codon table    
codons = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
    }


"""Definitions"""

def load_sequence():
    # Loads file name
	try:
		# Try: opening and using tkinter GUI. If any errors, you have to manually type it in
		import tkinter # GUI module
		from tkinter import filedialog # Choose file function
		from tkinter.filedialog import askopenfilename # 
		root = tkinter.Tk() # Makes a root window
		root.withdraw() # Withdraws window (since root window is not needed)
		sequence_file = askopenfilename(parent=root,initialdir=cwd,title='Please select a file') # Opens the GUI to pick a file
		#PS: A fasta file is not needed. Almost any file with proper structure would work
	except:
		sequence_file = input('Unable to use GUI. Type your file name with extension: ')

        
	"""Note: Multi compatible with different files"""
			
	# Opens and reads the file
	with open(sequence_file,'r') as f:
		DNA_sequence = f.readlines()

	# Checks where the file start and ends
	for i in DNA_sequence:
		match = re.match("^[atgc]*$", i.lower()) # Lower case to improve compatibility
		if match is None: # If line contains something else than a,t,g or c
			if start_of_sequence is not None:
				end_of_sequence = i.index(i) # Previous line is the end
			pass # Pass if line contains something else
		
		else: # If line only contains a,t,g and c
			if start_of_sequence is None:
				start_of_sequence = i.index(i) # Previous line must be non-sequence info           
                
	# Cuts away other parts
	DNA_sequence = DNA_sequence[start_of_sequence:end_of_sequence]
    
    # Makes the sequence into a string (sequence is at this moment a list)
    DNA_sequence = [line.replace('\n','') for line in DNA_sequence] # Removes \n from list
    DNA_sequence = ''.join(DNA_sequence) # Joins list into string 
    DNA_sequence = DNA_sequence.upper() # Makes the sequence into high case
    
    # Return string
    return DNA_sequence
    

# Function that determines what RNA sequence is made from a DNA sequence
def DNA2RNA(DNA_sequence)
    """Theory: When a gene is read, only one strand is read and transcribed to mRNA.
    The mRNA that is transcribed is the complimentary of the read strand, the anti-sense strand.
    However, you have to take in account for the direction of transcription and translation of the strand (5' to 3').
    The the sense strand (coding strand) has the same sequence as the mRNA but with U instead of T.
    Simplified solution: The coding strand (the gene) is the same as the mRNA sequence, but with U instead of T."""    
    
    mRNA_sequence=DNA_sequence.replace('T','U')
    
    return mRNA_sequence







"""
The definition "load_sequence()" can be used to store as a string.
Example:

DNA_sequence = load_sequence() <-- opens up a window and you choose a file that automatically loads it as string

mRNA_sequence = DNA2RNA(DNA_sequence) <-- Will return string as usual

mRNA_sequence = DNA2RNA(load_sequence()) <-- Will open up a window, lets you choose a file and then returns string

"""


"""Old code. Saving for lncxd. Note: I have renamed "fastaFile" to "sequence_file""""

"""
# Function that determines what protein is made from a DNA sequence
def DNA2AA(fastaFile,codons):
    AAsequence = ''
    with open(fastaFile,'r') as fileObj: # Added 'r' to the open
        for line in fileObj:
            line.strip()
        cont = fileObj.read()
        sequenceSearch=re.compile(r'')                                                #need to complete
        content = sequenceSearch.search(cont)
        print(content.group())
        for i in range(0,len(content.group()),3):
            seq = cont[i:i+3]
            AAsequence += codons[seq]
    return AAsequence
"""

    
