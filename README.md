arcmap-roms-regrid
==================

ArcMap toolbox and script that interfaces with paegan to regrid ROMS datasets and write to a new file with the new coordinate axes.

##Installation

To install the ROMS regridding toolbox for ArcMap, follow the steps below:

1. Make sure that you are running ArcMap Version 10.1 with Service Pack 1 installed
2. Install the [[ArcMap Multidimension Supplemental Tools][http://www.arcgis.com/home/item.html?id=9f963f362fe5417f87d44618796db938]], following  the installation steps provided in the ZIP archive.
3. Download the `paegan` library for Python from [[here][https://github.com/asascience-open/paegan/archive/master.zip]].
4. Unpack and ZIP archive, and from the folder containing `setup.py` run the following command in the terminal:

```bash
python setup.py install
```

5. Download the ZIP archive for [[this project][https://github.com/asascience-open/arcmap-roms-regrid/archive/master.zip]] and unpack to any desired location.

6. Open ArcMap and right-click the toolbox menu in order to add the new toolbox. Browse the file system and find the toolbox in the location specified previously. Select the `ROMS Regridder.tbx` file.

##Run It

To run the ROMS regridding tool, select the only tool under the ROMS Regridder toolbox from the toolbox menu. Fill out the form with the required (and optional, if desired) parameters.

To open the newly created netCDF file, which has been regridded based on the previous inputs to the tool, use the `Multidimension Tools` toolbox from the ArcMap toolbox menu.

