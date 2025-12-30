# Project 1: In-silico Characterization of the Human CFTR Protein

## Background
The Cystic Fibrosis Transmembrane Conductance Regulator (CFTR)
is a chloride ion channel protein encoded by the CFTR gene.
Mutations in CFTR cause cystic fibrosis, a life-threatening
genetic disorder affecting the lungs and digestive system.
Understanding the structure and function of CFTR is critical
for disease diagnosis and therapeutic development.

## Research Question
What are the structural, functional, and physicochemical
properties of the CFTR protein, and how do they relate to
its biological role?

## Gene and Protein Information
- Organism: Homo sapiens
- Gene name: CFTR
- UniProt ID: P13569
- Protein length: 1480 amino acids

## Methodology
### 1. Sequence Retrieval 
- Protein sequence obtained in FASTA format from UniProt
  <img width="1426" height="733" alt="Screenshot 2025-12-31 030018" src="https://github.com/user-attachments/assets/61670420-73ab-428c-bc89-c79683855cf8" />


### 2. Sequence Similarity Analysis
- Tool: BLASTp
- Database: NCBI non-redundant (nr)
  <img width="1920" height="1024" alt="Screenshot 2025-12-31 021644" src="https://github.com/user-attachments/assets/87dbf374-fb5d-4ca0-9109-ebc124ba653d" />


### 3. Domain and Motif Analysis
- Tools: InterProScan, Pfam
- Domains: Two nucleotide-binding domains (NBDs) and multiple transmembrane domains
  <img width="1870" height="961" alt="Screenshot 2025-12-31 022603" src="https://github.com/user-attachments/assets/3ae07a51-465e-4b3d-a7ce-5f2264a93f77" />


### 4. Physicochemical Characterization
- Tool: ExPASy ProtParam
- Parameters: Molecular weight, isoelectric point, instability index, aliphatic index
  <img width="1920" height="981" alt="Screenshot 2025-12-31 023348" src="https://github.com/user-attachments/assets/862b3243-03b2-484c-a765-3f548de35113" />
  <img width="1920" height="1030" alt="Screenshot 2025-12-31 023444" src="https://github.com/user-attachments/assets/e8214b4c-2193-41b2-a239-1ea8170a91bc" />



### 5. Transmembrane Helix Prediction
- Tool: TMHMM
- Purpose: Identification of membrane-spanning regions
  <img width="1920" height="974" alt="Screenshot 2025-12-31 024255" src="https://github.com/user-attachments/assets/34f6c341-4fbe-4df9-bd64-476bfe843132" />
  <img width="1920" height="938" alt="Screenshot 2025-12-31 024402" src="https://github.com/user-attachments/assets/e9e21bfa-124c-43aa-83d5-de17536a3d4b" />



## Results
BLASTp analysis confirmed high similarity with CFTR homologs
across vertebrates. Domain analysis identified conserved
ABC transporter domains and transmembrane helices essential
for ion channel activity. Physicochemical analysis suggests
that CFTR is a stable, hydrophobic membrane protein.

## Biological Interpretation
CFTR functions as an ATP-regulated chloride channel.
The presence of conserved ABC transporter domains supports
its role in ion transport and epithelial fluid regulation.

## Limitations
- Structural predictions are computational
- No experimental or clinical validation performed

## Future Wet-Lab Validation
- Expression analysis in epithelial cell lines
- Functional chloride channel assays
- Mutation analysis for disease-associated variants

## Conclusion
This in-silico analysis provides a comprehensive overview
of the CFTR protein and highlights the importance of
bioinformatics approaches in understanding genetic diseases.
