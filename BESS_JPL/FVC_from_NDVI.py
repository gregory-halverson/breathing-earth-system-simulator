from typing import Union

import numpy as np
import rasters as rt
from rasters import Raster


def FVC_from_NDVI(NDVI: Union[Raster, np.ndarray]) -> Union[Raster, np.ndarray]:
    """
    Convert Normalized Difference Vegetation Index (NDVI) to Fractional Vegetation Cover (FVC).

    Parameters:
        NDVI (Union[Raster, np.ndarray]): Input NDVI data.

    Returns:
        Union[Raster, np.ndarray]: Converted FVC data.
    """
    NDVIv = 0.52  # +- 0.03
    NDVIs = 0.04  # +- 0.03
    FVC = rt.clip((NDVI - NDVIs) / (NDVIv - NDVIs), 0.0, 1.0)

    return FVC
