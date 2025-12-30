# CFTR ΔF508 Mutation Analysis
# Author: Niketa Rajput

# Wild-type CFTR sequence (partial, region around F508)
wild_type = "ISFGLKDLV"

# Mutant CFTR sequence (ΔF508 deletion)
mutant = "ISGLKDLV"

# Step 1: Compare lengths
print("Wild-type length:", len(wild_type))
print("Mutant length:", len(mutant))

# Step 2: Identify deletion
for i in range(len(mutant)):
    if wild_type[i] != mutant[i]:
        print("Mutation detected at position:", i + 1)
        print("Wild-type amino acid:", wild_type[i])
        print("Mutant amino acid:", mutant[i])
        break
else:
    print("Deletion detected: Phenylalanine (F) at position 508")
