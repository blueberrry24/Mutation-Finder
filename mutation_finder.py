def find_mutations(ref_seq,mut_seq):
  ref_seq = ref_seq.upper() #converting sequence to upper case to avoid errors due to case sensitive feature of python
  mut_seq = mut_seq.upper()
  mutation_count=0  #initial count =0
  for i in range (len(ref_seq)): 
      if ref_seq[i] !=mut_seq[i]:
        print("position",i+1, ":", ref_seq[i],"->" , mut_seq[i])    #shows the change in the nucleotide(mutation position) 
        mutation_count+=1       #counts the no. of mutations 
      if len(ref_seq) != len(mut_seq):
        print("Error: Sequences must be of equal length")
        return 0
  return mutation_count
print("DNA Mutation Finder")
print("-------------------")
#main
ref = input("Enter reference DNA sequence: ")
mut = input("Enter mutated DNA sequence: ")

total = find_mutations(ref, mut)

print("Total mutations found:", total)
