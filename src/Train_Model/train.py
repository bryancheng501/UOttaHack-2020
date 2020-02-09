from imageai.Prediction.Custom import ModelTraining
model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory(r"./Pokemon_Images")
model_trainer.trainModel(num_objects = 151, num_experiments = 35, enhance_data = True, show_network_summary = True)