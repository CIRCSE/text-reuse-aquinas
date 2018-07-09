'''
Created on 09.07.2018

@author: mm
'''

import os.path as path
import os


############################## MAIN FUNCTION ############################

if __name__ == '__main__':
    
    tracer_results = path.abspath(path.join(__file__ ,"../../../05-results/scg-philosophiaeConsolationis/results-tracer-all.expanded.txt"))
    
    tracer_results_file = open(r""+ tracer_results)
    #tracer_results_file = open(r"results-tracer-all.expanded.txt")
    tracer_results_data = tracer_results_file.read().splitlines() 
    
    #output_file = path.abspath(path.join(__file__ ,"../../../05-results/scg-DeTrinitate/results-false-negatives_w_o_dupl.txt"))   
    #out = open(output_file, 'w')      
    
    
    out = open("philosophiaeConsolationis_results-tracer-all.expanded_w_o_dupl.txt", 'w') 
        
    
    id_dict = {}
    for line in tracer_results_data:
        line_array = line.split("\t")
        #print line
        #v = -1
        #try:
        #    v = id_dict[line_array[0]+":"+line_array[1]]
        #    print v + "++"
        #    print "dupl.:" + line_array[0]+":"+line_array[1] +" or " + line_array[1]+":"+line_array[0]
        #except:
        id_dict[line_array[0]+":"+line_array[1]] = 0
            
        #try:
            #v = id_dict[line_array[1]+":"+line_array[0]]
           # print v + "++"
           # print "dupl.:" + line_array[1]+":"+line_array[0] +" or " + line_array[0]+":"+line_array[1]
             
        #except:        
        id_dict[line_array[1]+":"+line_array[0]] = 0
        
    # rerun to get data
    '''for k in id_dict.keys():
        print str(id_dict[k]) +"##"
        print str(id_dict[k.split(":")[1]+":"+k.split(":")[0]]) + "###"'''
    
    for line in tracer_results_data:
        line_array = line.split("\t")
        
        id1 = line_array[0]
        id2 = line_array[1]
        
        if id_dict[id1+":"+id2] == 1 and id_dict[id2+":"+id1] == 1:
            print id1+"\t"+id2
            pass
        elif id_dict[id1+":"+id2] == 0 or id_dict[id2+":"+id1] == 0:
            out.write(line + "\n")
            id_dict[id1+":"+id2] = 1
            id_dict[id2+":"+id1] = 1
    
                
    out.close()       