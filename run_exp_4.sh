#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --export=PYTHONPATH="/home/andre.veski/python/lib/python3.4/site-packages"
module load python-3.4.0
python3 ssp_experiment_4.py ${SLURM_JOB_ID}
