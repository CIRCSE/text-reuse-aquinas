There are two scripts in this directory:

#######################
ITQuotationExtractor.py
#######################

It extracts only verses from the reuse annotated Gold data that contain actual annotations. The files needs to be in the "in" directory.
It required a folder "out" as it writes the extractions into: "out/extracted-quotations.csv".
The literature reference is the key, tabs-eparated, the relevant sentence follows with citations style annotated in round brackets directly following a word.
Words are tab-separated.


############################
TracerOutputVSGoldMatcher.py
############################

The script requires:
1) A folder "tracer_data" with files in it that have 4 -column format (TAB separated): ID TAB sentence_with_white_spaces TAB ID TAB sentence_with_white_spaces
2) An empty folder "matches".
3) A folder "out" with the file "extracted-quotations.csv" in it, that the other script created. 

It will write for every file from the "tracer_data" directory a new output file into "matches" that uses the trace file as prefix and ends itself in "_stats.csv"
This file if formatted in three TAB separated columns:
TRACER_sentence_id TAB #score# TAB the_TRACER_sentence

#score# is: the sum of the words from the tracer sentence that were found in the gold vocab, where a function word is counted only 0.5 a non-function word is counted 1.

Function words are default set to the top 500 words. You can change it in the variable "topwords".
