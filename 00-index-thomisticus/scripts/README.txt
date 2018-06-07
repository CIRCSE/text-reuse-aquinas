There are two scripts in this directory:

#######################
ITQuotationExtractor.py
#######################

It extracts only verses from the reuse annotated Gold data that contain actual annotations. The files need to be in the "in" directory.
It writes the extractions into: "out/extracted-quotations.csv".
The literature reference is the key, tabs-eparated, the relevant sentence follows with citations style annotated in round brackets directly following a word.
Words are tab-separated.


############################
TracerOutputVSGoldMatcher.py
############################

The script requires:
1) in the folder "tracer_data" need to exist files that have a 4-column format (TAB separated): ID TAB sentence_with_white_spaces TAB ID TAB sentence_with_white_spaces
3) the file "out/extracted-quotations.csv" needs to exist.

It will write for every file from the "tracer_data" directory a new output file into "matches" that uses the trace file as prefix and ends itself in "_stats.csv"
This file if formatted in three TAB separated columns:
TRACER_sentence_id TAB #score# TAB the_TRACER_sentence

#score# is: the sum of the words from the tracer sentence that were found in the gold vocab, where a function word is counted only 0.5 a non-function word is counted 1.

Function words are default set to the top 500 words. You can change it in the variable "topwords".
