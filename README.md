arcmap-roms-regrid
==================

ArcMap toolbox and script that interfaces with paegan to regrid ROMS datasets and write to a new file with the new coordinate axes.

## Installation

To install the ROMS regridding toolbox for ArcMap, follow the steps below:

1. Make sure that you are running ArcMap Version 10.1 with [Service Pack 1](http://support.esri.com/en/downloads/patches-servicepacks/view/productid/160/metaid/1913#choose-product) installed
2. Download and Install _ArcGIS 1.0 SP1 for Desktop Background Geoprocessing (64-bit)_ from [here](http://support.esri.com/en/downloads/patches-servicepacks/view/productid/160/metaid/1913#choose-product)

  **Be sure to install the following packages inside of the 64-bit Python installation that was installed or used as part of the above step!**
3. Download and Install the _SciPy_ package from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy).  Use the `scipy-0.12.0.win-amd64-py2.7.exe` file.
4. Download and Install the _NumPy_ package from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy).  Use the `numpy-MKL-1.7.1.win-amd64-py2.7.exe` file.
5. Download and Install the _NetCDF4_ package from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#netcdf4).  Use the `netCDF4-1.0.5dev.win-amd64-py2.7.exe` file.
6. Download _Paegan_ package from [here](https://github.com/asascience-open/paegan/archive/master.zip).
7. Unpack the _paegan_master.zip_ archive and, from the folder containing _setup.py_, run the following command in the terminal: `PATH_TO_64BIT_ARC_PYTHON/python.exe setup.py install`.
8. Download [this project](https://github.com/asascience-open/arcmap-roms-regrid/archive/master.zip) and unpack to any desired location.
9. Open ArcMap and right-click the toolbox menu in order to add the new toolbox. Browse the file system and find the toolbox in the location specified previously. Select the _ROMS Regridder.tbx_ file.

##Run It

To run the ROMS regridding tool, select the only tool under the ROMS Regridder toolbox from the toolbox menu. Fill out the form with the required (and optional, if desired) parameters.

To open the newly created netCDF file, which has been regridded based on the previous inputs to the tool, use the _Multidimension Tools_ toolbox from the ArcMap toolbox menu.

