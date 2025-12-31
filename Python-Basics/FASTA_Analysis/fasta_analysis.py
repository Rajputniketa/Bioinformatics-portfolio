# Automated FASTA File Analysis
# Author: Niketa Rajput

# Step 1: Read FASTA file
with open("CFTR.fasta", "r") as file:
    lines = file.readlines()

# Step 2: Remove header and join sequence
sequence = ""
for line in lines:
    if not line.startswith(">"):
        sequence += line.strip(

# Step 3: Basic analysis
length = len(sequence)
a_count = sequence.count("A")
g_count = sequence.count("G")
c_count = sequence.count("C")

# Step 4: Print results
print("Sequence length:", length)
print("A count:", a_count)
print("G count:", g_count)
print("C count:", c_count)
