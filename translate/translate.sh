#!/bin/bash

NUM_ROWS=160828  # give the no.of documents you need to translate
#NUM_ROWS=160
NUM_MACHINES=100


STEP=$(expr ${NUM_ROWS} / ${NUM_MACHINES} - 1)
for (( COUNTER=0; COUNTER<=${NUM_ROWS}; COUNTER+=STEP)); do
 
    start=$COUNTER
    stop=$(expr ${COUNTER} + ${STEP})
    if [ $stop -gt $NUM_ROWS ]
      then
        stop=$NUM_ROWS
    fi
    sbatch translate_slurm.sh $start $stop
done

