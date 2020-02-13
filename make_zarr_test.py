from dask_jobqueue import SLURMCluster 
from dask.distributed import Client 
  
cluster = SLURMCluster(cores=28,name='make_zarr',walltime='00:20:00',job_extra=['--constraint=BDW28','--exclusive','--nodes=1'],memory='20GB') 
  
cluster.scale(1) 
cluster.adapt(minimum=1, maximum=4) 
  
print(cluster.job_script()) 

from dask.distributed import Client 
client = Client(cluster) 
client 
  
import xarray as xr 
import dask 
import dask.threaded 
import dask.multiprocessing 
from dask.distributed import Client 
import zarr 
import numpy as np 
import os 
import time 
%timeit ds=xr.open_mfdataset('/scratch/cnt0024/hmg2840/albert7a/eNATL60/eNATL60-BLBT02-S/1h/surf/*2010m01*sozocrtx.nc', parallel=True, concat_dim='time_counter',chunks={'time_counter':672,'y':120,'x':120}) 


