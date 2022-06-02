from pathlib import PurePath as Path

DIR_ROOT = str(Path(__file__).parent.parent.parent)
DIR_OUTPUT = str(Path(DIR_ROOT + "/output"))
PATH_TRAIN_DATASET_PLOT = str(Path(DIR_OUTPUT + "/plot_train_dataset"))
