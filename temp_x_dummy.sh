#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -pe smp 32
#$ -V
#$ -q long.q

charmrun  +p32  namd2 temp_60_v1.conf > temp_60_v1/temp_60_op.log
