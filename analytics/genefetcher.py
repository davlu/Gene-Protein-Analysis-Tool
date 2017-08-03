# Handles and fetches DNA data from NCBI

# NCBI api
def get_sequence(GI,save='No'): # Example: GI=166706892

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
    
    # If you want the sequence as a list instead of string. When commented, the script returns a long string
    """sequence = list(sequence) # Make into list"""

    # If save is "Yes" or "yes", save as a file
    if (save is 'Yes' or save is 'yes'):
        with open((str(GI)+' DNA_sequence'+'.txt','w') as f: # PS: Directory not set, saves in local work directory
            for i in sequence: # Should not matter if list or string
                f.write(sequence)
    
    #Done
    return sequence



