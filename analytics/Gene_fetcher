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
