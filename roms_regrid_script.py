import os, sys
import numpy as np
import paegan.roms.roms as roms
from dateutil.parser import parse as dutil_parse
import netCDF4

def parse_args(args):
    try:
        infile = args[1]
    except:
        raise IndexError("Path to ROMS Model file must be included as the first command line argument to this script.")
    try:
        outfile = args[2]
    except:
        raise IndexError("Path to regridded output file must be included as the second command line argument to this script.")
    if not os.path.exists(infile):
        raise ValueError("ROMS Model Output file doesn't appear to exist, please specify a path to an existing netcdf file.")
    if os.path.exists(outfile):
        raise ValueError("Output file already exists! Please remove the existing file or choose a new name for the output file.")
    
    lon_new = np.arange(float(args[3]), float(args[4]), float(args[5]), dtype=np.float32)
    lat_new = np.arange(float(args[6]), float(args[7]), float(args[8]), dtype=np.float32)
    
    if np.any(np.asarray(args[9:12]) == "#"):
        s_new = None
    else:
        s_new = np.arange(float(args[9]), float(args[10]), float(args[11]), dtype=np.float64)

    if np.any(np.asarray(args[12:15]) == "#"):
        time_new = None
    else:
        t_bounds = (dutil_parse(args[12], dayfirst=False), dutil_parse(args[13], dayfirst=False))
        with netCDF4.Dataset(infile) as nc:
            time_units = nc.variables["ocean_time"].units
            time_type = nc.variables["ocean_time"][0].dtype
            if "day" in time_units:
                dt = float(args[14]) / 24.
            elif "sec" in time_units:
                dt = float(args[14]) * 3600.
            elif "min" in time_units:
                dt = float(args[14]) * 60.
        t_bounds = netCDF4.date2num(t_bounds, units=time_units)
        time_new = np.arange(t_bounds[0], t_bounds[1], dt, dtype=time_type)
    return infile, outfile, lon_new, lat_new, s_new, time_new

def main(infile, outfile, lon_new, lat_new, s_new, time_new):
    roms.regrid_roms(outfile, infile, lon_new, lat_new, z=s_new, t=time_new)

if __name__ == "__main__":
    print sys.argv
    if sys.argv[1] in "--help":
        print "Use:\npython roms_regrid_script.py lon_min lon_max delta_lon lat_min lat_max delta_lat <s_min s_max delta_s> <time_min time_max delta_time>\n\n    lon_min:    None\n    lon_max:    None\n    delta_lon:  None\n..."
    else:
        args = parse_args(sys.argv)
        main(*args)
