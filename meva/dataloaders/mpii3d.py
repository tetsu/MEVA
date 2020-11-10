# This script is borrowed from https://github.com/mkocabas/VIBE
# Adhere to their licence to use this script

from meva.dataloaders import Dataset3D
from meva.utils.video_config import MPII3D_DIR


class MPII3D(Dataset3D):
    def __init__(self, set, seqlen, overlap=0, debug=False):
        db_name = 'mpii3d'

        # during testing we don't need data augmentation
        # but we can use it as an ensemble
        set = "all"
        is_train = set == 'train' or set =="all"
        overlap = overlap if is_train else 0.
        print('MPII3D Dataset overlap ratio: ', overlap)
        super(MPII3D, self).__init__(
            set = set,
            folder=MPII3D_DIR,
            seqlen=seqlen,
            overlap=overlap,
            dataset_name=db_name,
            debug=debug,
        )
        print(f'{db_name} - number of dataset objects {self.__len__()}')