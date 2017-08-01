# Handles and fetches DNA data from NCBI

# NCBI api
def get_sequence(GI): # Example: GI=166706892

    # Imports from biopython
    from Bio import Entrez

    # Can be any mail, doesn't really matter
    Entrez.email ="BioPython@gmail.com"

    # Sends a request for GI
    request = Entrez.epost("nucleotide",
                           id=[str(GI)])

    # Reads the results, which contains everything you need to fetch it
    result = Entrez.read(request)

    # Sets parameters for feching data
    webEnv = result["WebEnv"]
    queryKey = result["QueryKey"]

    # Fetches genes
    handle = Entrez.efetch(db="nucleotide",
                           retmode="xml",
                           webenv=webEnv,
                           query_key=queryKey)

    #Needs to have Entrez.parse as list
    for r in Entrez.parse(handle):

        #Prints data
        print(">GI = ",
                GI,
                " ",
                r["GBSeq_primary-accession"],
                " ",
                r["GBSeq_definition"])

    #Handles sequence
    sequence = r["GBSeq_sequence"].upper() # Make into higher case
    sequence = list(sequence) # Make into list

    #Done
    return sequence



# Fetch sequence from local file
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
    
