import numpy as np


def gen_samples(gen_dic_list,min_max_dic,X_train,number,target_class=None):
    
    
    generated_samples=[]
    
    feature_keys=[]
    
    r,c=X_train.shape
    
    for k,v in min_max_dic.items():
        feature_keys.append(k)
        
    gen_dic_keys=[]
    
    
        
    for gen_index in range(0,len(gen_dic_list),1):
        
        gen_dic_keys=[]
        
        
        for k,v in gen_dic_list[gen_index].items():
            gen_dic_keys.append(k)
            #None
        
        for n in range(0,number,1):
        
            sample_vector=np.zeros(c)
        
            
            for k in range(0,len(sample_vector),1):
                if k in gen_dic_keys:
                    
                    tmp=np.random.uniform(gen_dic_list[gen_index][k][0],gen_dic_list[gen_index][k][1],1)
                    sample_vector[k]=tmp[0]
                    
                elif k in feature_keys:
                    
                    tmp=np.random.uniform(min_max_dic[k][0],min_max_dic[k][1],1)
                    sample_vector[k]=tmp[0]
            
            
            generated_samples.append(sample_vector)
        
    print(generated_samples)
    
    return generated_samples