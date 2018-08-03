'''
Created on 01.08.2018

@author: mm
'''
import os.path as path
import os


def get_joined_features(array1, array2):
    joint_features = []
    for FID in array1:
        if FID in array2:
            joint_features.append(FID)
    jf = set(joint_features)
    if len(jf) > 0:
        return jf
    return None
            
    
if __name__ == '__main__':
    
    #### change these paths or chage the names of the sel, link and feats files. make sure you store all files in the same directory as where this script is in #### 
    #################################################################
    
    feature_file = open(r"tagged.feats")
    selection_file = open(r"tagged.sel")
    linking_file = open(r"tagged-tagged.link")
    #feature_file = open(r"test.feats")
    #selection_file = open(r"test.sel")
    #linking_file = open(r"test.link")
    feature_data = feature_file.read().splitlines() 
    selection_data = selection_file.read().splitlines() 
    linking_data = linking_file.read().splitlines() 
    
    out = open(feature_file.name[:-6] + ".viz.txt",'w')
    
    #################################################################
    feat_dict = {}
    feats_in_sentences = {}
    
    
    # 1st, let's just save the feature next to its ID in a dictionary (FID is key)
    for line in feature_data: 
        line_arr = line.split("\t")
        FID = line_arr[0]
        feature = line_arr[1]
        feat_dict[FID] = feature
    
    print "Feature list read."
    
    # 2nd, lets' save all feature IDs next to sentence IDs (SIDs are keys)
    for line in selection_data:
        line_arr = line.split("\t")
        FID = line_arr[0]
        SID = line_arr[1]
        new_array = []
        if SID in feats_in_sentences.keys():
            new_array = feats_in_sentences[SID] 
        new_array.append(FID)
        feats_in_sentences[SID] = new_array
    
    print "Saved features to sentences."   
    
    
    # 3rd, now we find two SIDs linked from the linking data and can look up whether/how many/which feature IDs they share
    for line in linking_data:
        line_arr = line.split("\t")
        SID1 = line_arr[0]
        SID2 = line_arr[1]
        try:
            FIDs1 = feats_in_sentences[SID1]
            FIDs2 = feats_in_sentences[SID2]
            join = get_joined_features(FIDs1, FIDs2)
            if join is not None:
                out.write(SID1 + "\t" + SID2 + "\t")
                print SID1 + "\t" + SID2 + "\t",
                for feature in join:
                    out.write(feat_dict[feature] + " ")
                    print feat_dict[feature] + " ",
                out.write("\t" + line_arr[2] + "\n")
                print "\t" + line_arr[2]
        except:
            pass
        
        

    
    
    
    
    
    
    

          