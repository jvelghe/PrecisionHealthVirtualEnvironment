
import deeplabcut as dlc

#config_path = dlc.create_new_project('Project_name', 'Experimenter', ['videofile_path'], working_directory = 'path_where_you_want_the_project_files', videotype='mp4', copy_videos = True)
config_path = dlc.create_new_project('test', 'me', ['/scratch/tr-precisionhealth-1/Workshops/StudentSpaces/$CWL/DLC_intro/data/00029.avi'], working_directory = '/scratch/tr-precisionhealth-1/Workshops/StudentSpaces/$CWL/DLC_intro/projects/', videotype='avi', copy_videos = True)

dlc.extract_frames(config_path, 'automatic','kmeans',crop=False)

dlc.label_frames(config_path)

dlc.create_training_dataset(config_path)

dlc.train_network(config_path, saveiters = 250, maxiters = 1000, displayiters = 100)

dlc.evaluate_network(config_path)

dlc.analyze_videos(config_path, ['/scratch/tr-precisionhealth-1/Workshops/StudentSpaces/$CWL/DLC_intro/data/'], save_as_cv = True)

dlc.create_labeled_video(config_path, ['/scratch/tr-precisionhealth-1/Workshops/StudentSpaces/$CWL/DLC_intro/data/'])
