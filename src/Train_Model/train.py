from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
prediction.setDataDirectory("C:/Users/bryan/Documents/Carleton 19-20/Ottahack/UOttaHack-2020/src/Scrape_Images/Pokemon_Images")
model_trainer.trainModel(num_objects = 151, num_experiments = 50, enhance_data = True, show_network_summary = True)
