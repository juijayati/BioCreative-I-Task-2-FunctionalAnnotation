BIOCREATIVE CORPUS 

The BioCreative corpus comprises two subsets or sub-corpora.
 
The BioCreative corpus I was derived originally from the 
evaluation of task 2.1 of the BioCreative 2003 challenge and
the BioCreative corpus II from task 2.2. The first corpus 
consists in an annotation passage retrieval corpus of human 
proteins and the second one in an annotation prediction passage 
corpus. The annotations are based on Gene Ontology (GO) terms. 
The passages were extracted from full text articles in SGML 
format of the Journal of Biological Chemistry (JBC) and evaluated
by GO annotators at the European Bioinformatics Institute (EBI), 
taking into account the context of each passage within the whole 
document, meaning that those passages where highlighted within 
the full text articles. Notice that the actual passages are 
not-parsed SGML (to be able to locate those passages within the 
full text SGML documents). Therefore the overall corpus documents 
are not compliant with standard XML. Nevertheless the tags which 
describe the corpora are given below together with useful links. 

BioCreative corpus I: Contained in the file BioCreativeCorpusI.txt, 
corresponds to the human protein annotation passage retrieval corpus. 

BioCreative corpus II: Contained in the file BioCreativeCorpusII.txt, 
corresponds to the human protein annotation passage retrieval and 
prediction corpus. 

Corpus-tag: Root tag of the corpus. 


ENTRY-tag: Child tag defining each of the prediction entries 

ENTRY_ NR-tag: Sub-child tag defining the serial identifier for 
each of the en- tries in the corpus. 

ENTRY_ID-tag: Sub-child tag defining the serial identifier for 
each of the entries in the corpus. Sub-child tag if the composed 
entry identifier, which is build up by the SwissProt accession 
number, the Gene Ontology code, the PubMed identifier, the 
submission identifier and the run identifier 

PMID-tag: Sub-child tag defining the PubMed identifier of the 
document which contains the text passage. 

SP_ACC-tag: Sub-child tag defining the SwissProt accession number 
of the hu- man protein entity. 

PROT_EVAL-tag: Sub-child tag defining the evaluation type of the 
protein en- tity: 2=correct prediction, 1= general prediction 
(overall correct but to general for practical use, e.g. The 
protein family was identified but not the specific protein) and 
0= wrong prediction 

GOID-tag: Sub-child tag defining the Gene Ontology identifier of 
the concept used fro annotation. RUNID-tag: Sub-child tag defining 
the prediction run (user run) of the predicted passage. 

GO_EVAL-tag: Sub-child tag defining the evaluation type of the 
annotation term (GO term) entity: 2=correct prediction, 1= general 
prediction (overall correct but to general for practical use, e.g. 
Very general concept, close to the root node) and 0= wrong prediction 

GO_CONCEPT-tag: Sub-child tag defining the actual annotation term as 
con- tained in Gene Ontology 

GO_CLASS-tag: Sub-child tag defining the class of the Given GO term 
(P: Bi- ological Process class, F: Molecular Function class and C: 
Cellular Component class). 

IC_NORM-tag: Sub-child tag defining the normalized information content 
of the gene ontology term calculated using GOA frequencies of those terms. 

IC_PRONORM-tag: Sub-child tag defining the normalized propagated 
(accumulated) information content of the gene ontology term calculated 
using GOA frequen- cies of those terms and the corresponding child nodes
of that term. 

GO_LEVEL-tag: Sub-tag defining the minimal distance of the GO term to 
the root node of its class. 

GO_DENSITY-tag: Sub-tag defining the normalized density, i.e. number of 
child nodes. 

GO_LEN-tag: Sub-tag defining the number of word tokens forming the GO 
term after extensive word splitting (i.e. splitting at white-space and 
special characters such as hyphens and backslashes.) 

PASSAGE-tag: The actual annotation passage, it is NOT SGML parsed (to be able
to locate the text passage in the full text sgml documents of JBC) and 
comes from full text SGML formated of the journal of Biological Chemistry. 

Useful links: 

BioCreative: http://www.pdg.cnb.uam.es/BioLINK/BioCreative.eval.html 
JBC: http://www.jbc.org/ 
PubMed: http://www.ncbi.nlm.nih.gov/entrez/query.fcgi 
GO: http://www.geneontology.org/ 
GOA: http://www.ebi.ac.uk/GOA/ 
Swissprot: http://www.ebi.ac.uk/swissprot/ 
Other contest: http://www.pdg.cnb.uam.es/martink/index.html
