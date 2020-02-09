from imageai.Prediction import ImagePrediction
import sys
import os

#file = sys.argv[1]



execution_path = os.getcwd()
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(r"C:/Users/harol/Documents/UOttaHack-2020/src/Front_Back/resnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.loadModel()


predictions, percentage_probabilities = prediction.predictImage(r"C:/Users/harol/Documents/pikachu.png", result_count=5)
for index in range(len(predictions)):
	print(predictions[index] , " : " , percentage_probabilities[index])