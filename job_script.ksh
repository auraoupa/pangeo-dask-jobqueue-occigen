#!/usr/bin/env bash

#SBATCH -J make_zarr
#SBATCH -n 1
#SBATCH --cpus-per-task=28
#SBATCH --mem=19G
#SBATCH -t 00:20:00
#SBATCH --constraint=BDW28
#SBATCH --exclusive
#SBATCH --nodes=1
JOB_ID=${SLURM_JOB_ID%;*}



/scratch/cnt0024/hmg2840/albert7a/anaconda3/bin/python -m distributed.cli.dask_worker tcp://127.0.0.1:34869 --nthreads 28 --memory-limit 20.00GB --name make_zarr--${JOB_ID}-- --death-timeout 60


