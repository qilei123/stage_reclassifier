class reclassifier:
    def __init__(self):
        pass
        
    def encode_feature(self,detection_result):
        pass
    def reclassifier(self,pre_prediction_stage,detection_result):
        
        #predict_result = self.classifier(self.encode_feature(detection_result))
        
        if pre_prediction_stage==4 or pre_prediction_stage==0:
            return pre_prediction_stage
        
        lesions_count = [0,0,0,0]

        for box in detection_result['results']:
            lesions_count[int(box['label'])-1]+=1
        final_stage = pre_prediction_stage

        if lesions_count[2]==0 and lesions_count[3]==0 and lesions_count[1]<=3 and lesions_count[0]<=3:
            final_stage = 1
        elif (lesions_count[2]!=0 or lesions_count[3]!=0) and lesions_count[0]<20:
            final_stage = 2
        elif lesions_count[0]+lesions_count[1]>30:
            final_stage = 3
        return final_stage
