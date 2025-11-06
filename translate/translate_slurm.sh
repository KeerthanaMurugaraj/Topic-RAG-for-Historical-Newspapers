#!/bin/bash -l

#SBATCH -N 1
#SBATCH -c 1
#SBATCH --time=10:00:00
#SBATCH -p batch
#SBATCH  --ntasks-per-node=1

LOGFILE=translate_$1_$2.out
DATA_DIR=your directory
IP_FILE=${DATA_DIR}/ip_df_to_translate.pkl # give your .pkl file to translate.
COLUMNS=content_clean,title_clean
OP_DIR=$DATA_DIR

cd your directory
conda activate topic_modeling
srun python translate_content.py -f $1 -l $2 -i $IP_FILE -o $OP_DIR -t $COLUMNS &> ${LOGFILE}
