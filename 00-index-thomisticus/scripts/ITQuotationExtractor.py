'''
Created on 04.06.2018
@author: maria moritz & greta franzini
'''
import os

if __name__ == '__main__':

    # read the data directory
    fils = sorted(os.listdir("in"), key= lambda s: int(s.split(".")[2]))
    out = open("extracted-quotations.csv", 'w')
    #print fils
    
    QR = QS = QL = 0
    RS = RL = SL = 0
    RSL = 0
    ANYofThem = 0
    
    QRanyBool = False
    QSanyBool = False
    QLanyBool = False
    for fi in fils:

        f = open(r"in/"+fi)
        lst = f.read().splitlines()       
        # print fi + "\n"
        # run over the file content
        started = False
        text = ""
        quotes = False
        for line in lst:
            # print line
            if line.startswith('<s id='):
                
                id_ = line.split("*")[1][:-2]
                
                # print output
                if len(text) > 0 and quotes:
                    out.write(text + "\n")
                    text = ""
                
                    # update statistics
                    if QRanyBool and QSanyBool and QLanyBool:
                        RSL += 1
                    elif QRanyBool and QSanyBool:
                        RS += 1
                    elif QSanyBool and QLanyBool:
                        SL += 1
                    elif QRanyBool and QLanyBool:
                        RL += 1
                        
                    elif QRanyBool:
                        QR += 1
                    elif QSanyBool:
                        QS += 1
                    elif QLanyBool:
                        QL += 1
                    # any
                    if QRanyBool or QSanyBool or QLanyBool:
                        ANYofThem += 1
                    
                # saving ID only for mow and resetting parameters    
                text = id_ + "\t"
                quotes = False
                QRanyBool = False
                QSanyBool = False
                QLanyBool = False                    
                     
            elif line.startswith('<f>'):
                # look more detailed at the content
                word = line.split('<l>')[0].split('<f>')[1] 
                if '<x name="fp">QR' in line:
                    quotes = True
                    text = text + word + "(QR)" + "\t"
                    QRanyBool = True
                elif '<x name="fp">QS' in line:
                    quotes = True
                    text = text + word + "(QS)" + "\t"
                    QSanyBool = True
                elif '<x name="fp">QL' in line:
                    quotes = True
                    text = text + word + "(QL)" + "\t"
                    QLanyBool = True
                else:
                    text = text + word + "\t"
            
            
            
            elif line.startswith('<d>'):
                det = line.split('<l>')[0].split('<d>')[1]
                text = text[:-1]
                text = text + det + "\t"
                
                    
                    
                   
    out.close() 

    print "No. of sentences containing any: " + str(ANYofThem) + "\n"
    print "No. of sentences containing all of them: " + str(RSL) + "\n"
    
    print "No. of sentences containing only QRs and QSs: " + str(RS) + "\n"
    print "No. of sentences containing only QRs and QLs: " + str(RL) + "\n"
    print "No. of sentences containing only QSs and QLs: " + str(SL) + "\n"
    
    print "No. of sentences containing only QRs: " + str(QR) + "\n"
    print "No. of sentences containing only QSs: " + str(QS) + "\n"
    print "No. of sentences containing only QLs: " + str(QL) + "\n"


                    

                    
                
                
    