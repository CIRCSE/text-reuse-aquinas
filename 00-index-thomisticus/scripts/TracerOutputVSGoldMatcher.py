'''
Created on 06.06.2018

@author: mm
'''
import os


def find_matches(sent):
    
    # split a tracer sent
    sent_arr = sent.split(" ")
    
    # for every word from a tracer snippet, run over all gold data
    sim_counter = 0
    for w in sent_arr:
        # the values in the dictionary are arrays of words
        for value_arr in gold_dict.values():
            
            for val in value_arr:
                # get rid of the annotation
                if "(" in val and ")" in val:
                    v = val[:-4]
                    # match?
                    if w == v:
                        # function word mappings are counted only as half a match
                        if v in fw.keys():
                            sim_counter += .5
                        else:
                            sim_counter += 1.0
                        
    # return the sum of the matches for each sentence preceding the sentence itself
    return str(sim_counter/(len(sent_arr)*1.0)) + "\t" + sent


############################## MAIN FUNCTION ############################

if __name__ == '__main__':
    
    topwords = 500
    gold_dict = {}
    fw = {}
    gold_vocab = {}
        
    # gold data reading
    gold_file = open(r"out/extracted-quotations.csv")
    gold_data = gold_file.read().splitlines()          
    
    
    #################################################################
    
    # read the gold data into a dictionary

    for line in gold_data:
        line_arr = line.split("\t") 
        # save the gold data to the gold dictionary
        gold_dict[line_arr[0]] = line_arr[1:]
        
        # prepare the gold vocabulary
        tokens = line_arr[1:]
        for token in tokens:
            if "(" in token and ")" in token:
                word = token[:-4]
                freq = 0
                try:
                    freq = gold_vocab[word]
                    gold_vocab[word] = freq+1
                except:
                    gold_vocab[word] = 1
             
    # get the most frequent words from the vocab
    sorted_vocab = sorted(gold_vocab.items(), key=lambda x: x[1])   
    gold_vocab = reversed(sorted_vocab)
    
    c = 0
    for k in gold_vocab:
        c += 1
        if c > topwords:
            break
        fw[k[0]] = 0



    # tracer directory reading
    tracer_files = os.listdir("tracer_data")
    
    # read the tracer data
    for fil in tracer_files:
        
        file_tracer = open(r"tracer_data/" + fil)
        tracer_data = file_tracer.read().splitlines() 
        
        # output
        out = open("matches/" + fil[:-4] + "_stats.csv", 'w')
        
        for line in tracer_data:
            tracer_arr = line.split("\t")
            tracer_line1 = tracer_arr[1]
            tracer_line2 = tracer_arr[3]
            
            # find matches in tracer line_1 with the gold data
            out.write(tracer_arr[0] + "\t" + find_matches(tracer_line1) + "\n" )
            out.write(tracer_arr[2] + "\t" + find_matches(tracer_line2) + "\n" )
            
        out.close()
        
        